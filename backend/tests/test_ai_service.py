from app.services.ai_service import AIRequestService


def test_infers_request_name_from_ocr_text_with_fallback():
    service = AIRequestService(enabled=False)

    text = "This is an OCR scan with ADF1 RFI AR 12345 R1"

    result = service.infer_request_name(text)

    assert result == "ADF1-RFI-AR-12345-R1"
