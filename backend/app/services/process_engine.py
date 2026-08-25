from pathlib import Path
import fitz
import shutil

from app.services.image_service import ImageService
from app.services.ocr_service import OCRService
from app.core.job_status import job_status
import time


class ProcessEngine:

    def __init__(self):
        self.ocr = OCRService()

    def process(
        self,
        pdf_path: str,
        pages_per_request: int,
        output_folder: str,
        fixed_code: str | None = None,
        pdf_rotation: int = 0,
        ocr_rotation: int = 0,
        auto_rotate: bool = False,
    ):
        # 1. بداية المعالجة
        job_status["progress"] = 0
        job_status["status"] = "Reading PDF"

        document = fitz.open(pdf_path)

        output_folder = Path(output_folder)

        if output_folder.exists():
            shutil.rmtree(output_folder)

        output_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        total_pages = len(document)
        current_page = 0

        # تم التجهيز وبدء العمليات
        job_status["progress"] = 5
        job_status["status"] = "Processing Requests"

        while current_page < total_pages:

            request_pdf = fitz.open()

            for page in range(
                current_page,
                min(current_page + pages_per_request, total_pages)
            ):
                request_pdf.insert_pdf(
                    document,
                    from_page=page,
                    to_page=page
                )

            # تدوير صفحات الـ PDF الناتجة
            if pdf_rotation != 0:
                normalized_pdf_rot = pdf_rotation % 360
                for page in request_pdf:
                    page.set_rotation(normalized_pdf_rot)

            first_page = request_pdf[0]

            image = ImageService.page_to_image(first_page, rotation=ocr_rotation)

            request_region = ImageService.crop_request_region(image)

            temp_image = output_folder / "temp.png"
            request_region.save(temp_image)

            text = self.ocr.extract_text(str(temp_image))

            print("=" * 70)
            print(f"Start Page : {current_page}")
            print(f"OCR TEXT   : {text}")
            print("=" * 70)

            request_name = self.ocr.extract_request_name_from_text(text)

            if request_name is None:
                request_name = self.ocr.extract_request_name(str(temp_image))

            code_region = ImageService.crop_code_region(image)

            temp_code = output_folder / "code.png"
            code_region.save(temp_code)

            if fixed_code is not None:
                code = fixed_code.strip().upper()
            else:
                code = self.ocr.extract_code(str(temp_code))

            if request_name and code:
                request_name += f" CODE {code}"

            if request_name is None:
                request_region.save(
                    output_folder / f"FAILED_{current_page}.png"
                )
                request_name = f"UNKNOWN_{current_page}"

            pdf_name = output_folder / f"{request_name}.pdf"

            request_pdf.save(pdf_name)
            request_pdf.close()

            current_page += pages_per_request

            # 🎯 حساب الـ Progress الديناميكي (من 5% إلى 95%)
            processed_ratio = current_page / total_pages
            # مينفعش يتخطى 1.0 في آخر دورة
            processed_ratio = min(processed_ratio, 1.0) 
            
            percent = int(5 + (processed_ratio * 90))
            job_status["progress"] = percent
            job_status["status"] = f"Processed {min(current_page, total_pages)} of {total_pages} pages"

            # تنظيف الصور المؤقتة
            # Ensure image resources are closed before unlinking
            try:
                request_region.close()
            except Exception:
                pass

            try:
                code_region.close()
            except Exception:
                pass

            try:
                image.close()
            except Exception:
                pass

            def safe_unlink(path: Path, retries: int = 3, delay: float = 0.1):
                for _ in range(retries):
                    try:
                        if path.exists():
                            path.unlink()
                        return
                    except PermissionError:
                        time.sleep(delay)
                    except Exception:
                        return

            safe_unlink(temp_image)
            safe_unlink(temp_code)

        # 3. إنهاء المهمة
        document.close()
        job_status["progress"] = 100
        job_status["status"] = "Finished"