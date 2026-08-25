import re


class RequestParser:

    TYPES = ["AR", "ME", "EL", "CI"]

    @classmethod
    def parse(cls, text: str):

        text = text.upper()

        # إزالة المسافات
        text = text.replace(" ", "")

        # -----------------------------
        # تصحيح أخطاء OCR الشائعة
        # -----------------------------

        replacements = {

            "ADFI": "ADF1",
            "ADFL": "ADF1",

            "RFL": "RFI",
            "RFII": "RFI",

            "RO": "R0",
            "RD": "R0",
            "RQ": "R0",

            "RI": "R1",
            "RL": "R1",

            "EL": "ELC",

            "—": "-",
            "_": "-"

        }

        for wrong, correct in replacements.items():
            text = text.replace(wrong, correct)

        # -----------------------------------
        # استخراج الرقم
        # -----------------------------------

        number = re.search(r"\d{5}", text)

        if not number:
            return None

        number = number.group()

        # -----------------------------------
        # استخراج النوع
        # -----------------------------------

        request_type = None

        for t in cls.TYPES:

            if f"-{t}-" in text:

                request_type = t

                break

        if request_type is None:
            return None

        # -----------------------------------
        # استخراج Revision
        # -----------------------------------

        revision = re.search(r"R[0-9ODQIL]", text)

        if revision:

            revision = revision.group()

            revision = (
                revision
                .replace("O", "0")
                .replace("D", "0")
                .replace("Q", "0")
                .replace("I", "1")
                .replace("L", "1")
            )

        else:

            revision = "R0"

        return f"ADF1-RFI-{request_type}-{number}-{revision}"