import re


class TextNormalizer:

    @staticmethod
    def normalize(text: str) -> str:

        text = text.upper()

        # إزالة المسافات الزائدة
        text = re.sub(r"\s+", " ", text)

        # -----------------------------
        # تصحيح الكلمات الثابتة
        # -----------------------------

        text = text.replace("ADFI", "ADF1")
        text = text.replace("RFL", "RFI")
        text = text.replace("RFI-", "RFI-")

        # -----------------------------
        # تصحيح نوع الريكوست
        # -----------------------------

        text = text.replace("-A8-", "-AR-")
        text = text.replace("-AF-", "-AR-")
        text = text.replace("-MR-", "-ME-")

        # -----------------------------
        # تصحيح الـ Revision
        # -----------------------------

        text = re.sub(r"-RO\b", "-R0", text)
        text = re.sub(r"-RD\b", "-R0", text)
        text = re.sub(r"-RQ\b", "-R0", text)
        text = re.sub(r"-RD\d", "-R0", text)

        text = re.sub(r"-RI\b", "-R1", text)
        text = re.sub(r"-RL\b", "-R1", text)

        # -----------------------------
        # O بدل 0 داخل Revision
        # -----------------------------

        text = re.sub(r"RO\b", "R0", text)

        # -----------------------------
        # I بدل 1
        # -----------------------------

        text = text.replace("ADFI", "ADF1")

        return text