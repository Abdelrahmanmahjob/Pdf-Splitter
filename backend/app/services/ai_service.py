import os
import re
from typing import Optional


class AIRequestService:
    """Lightweight AI-assisted request-name inference layer.

    It uses a deterministic heuristic first, then can optionally call an
    external LLM service when configured. The goal is to improve OCR result
    recovery without breaking the existing pipeline.
    """

    REQUEST_PATTERN = re.compile(r"ADF\d?-?RFI-(AR|ME|EL|CI)-\d+-R\d+", re.IGNORECASE)
    OCR_VARIANT_PATTERN = re.compile(r"(ADF\s*\d?|ADF\s*I|ADF\s*L)\s*(RFI|RFL|RFI|RFII|R\s*F\s*I)\s*(AR|ME|EL|CI)\s*(\d{3,6})\s*(R\s*[0-9ODQIL])?", re.IGNORECASE)

    def __init__(self, enabled: bool = False, api_key: Optional[str] = None, model: str = "gpt-4o-mini"):
        self.enabled = enabled
        self.api_key = api_key or os.getenv("AI_API_KEY")
        self.model = model

    def infer_request_name(self, text: str) -> Optional[str]:
        if not text:
            return None

        cleaned = re.sub(r"\s+", " ", text).strip()
        match = self.REQUEST_PATTERN.search(cleaned)
        if match:
            return match.group().upper().replace("-", "-")

        variant = self.OCR_VARIANT_PATTERN.search(cleaned)
        if variant:
            adf = "ADF1"
            rfi = "RFI"
            request_type = variant.group(3).upper()
            number = variant.group(4)
            revision = variant.group(5)
            if revision:
                revision = revision.replace(" ", "").replace("O", "0").replace("D", "0").replace("Q", "0").replace("I", "1").replace("L", "1")
            else:
                revision = "R0"
            return f"{adf}-{rfi}-{request_type}-{number}-{revision.upper()}"

        if not self.enabled or not self.api_key:
            return None

        try:
            from openai import OpenAI

            client = OpenAI(api_key=self.api_key)
            response = client.responses.create(
                model=self.model,
                input=[
                    {
                        "role": "system",
                        "content": "You extract request IDs from OCR text. Return only the normalized request name like ADF1-RFI-AR-12345-R1. If not found, return NONE.",
                    },
                    {
                        "role": "user",
                        "content": cleaned,
                    },
                ],
            )
            answer = getattr(response, "output_text", "")
            normalized = answer.strip().upper()
            if normalized and normalized != "NONE":
                return normalized
        except Exception:
            return None

        return None
