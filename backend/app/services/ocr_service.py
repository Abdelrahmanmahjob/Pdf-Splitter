import os

# 1. إيقاف تسريع OneDNN لمنع تعارض PIR Attribute على الويندوز
os.environ["FLAGS_use_onednn"] = "0"
os.environ["FLAGS_enable_pir_api"] = "0"
os.environ["PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK"] = "True"

from paddleocr import PaddleOCR
from app.utils.request_parser import RequestParser
from app.services.ai_service import AIRequestService

import re


class OCRService:

    REQUEST_PATTERN = re.compile(
        r"ADF\d-RFI-(AR|ME|EL|CI)-\d+-R\d+"
    )

    CODE_PATTERN = re.compile(
        r"CODE\s*([BC])",
        re.IGNORECASE
    )

    def __init__(self):
        # 2. تهيئة PaddleOCR مع إيقاف الـ MKLDNN صراحةً
        self.ocr = PaddleOCR(
            lang="en",
            enable_mkldnn=False
        )
        self.ai_service = AIRequestService(
            enabled=os.getenv("AI_OCR_ENABLED", "false").lower() == "true",
            api_key=os.getenv("AI_API_KEY"),
        )
        
    def read_image(self, image_path):
        result = self.ocr.ocr(image_path)
        return result

    def extract_text(self, image_path):

        result = self.ocr.ocr(image_path)

        if not result:
            return ""

        texts = result[0]["rec_texts"]

        return " ".join(
            t.strip()
            for t in texts
            if t.strip()
        )
    
    def extract_request_name(self, image_path):
        text = self.extract_text(image_path)

        parsed = RequestParser.parse(text)
        if parsed:
            return parsed

        ai_guess = self.ai_service.infer_request_name(text)
        return ai_guess

    def extract_request_name_from_text(self, text):
        match = self.REQUEST_PATTERN.search(text)
        if match:
            return match.group()
        return None

    def extract_code(self, image_path):
        text = self.extract_text(image_path).upper()
        text = text.replace("8", "B")
        text = text.replace("13", "B")
        text = text.replace("|", "I")
        text = text.strip()

        if "B" in text:
            return "B"

        if "C" in text:
            return "C"

        return "None "