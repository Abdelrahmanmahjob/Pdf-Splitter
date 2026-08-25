from app.services.ocr_service import OCRService
from app.utils.text_normalizer import TextNormalizer

ocr = OCRService()

request_name = ocr.extract_request_name(
    "output/request_region.png"
)

print(request_name)