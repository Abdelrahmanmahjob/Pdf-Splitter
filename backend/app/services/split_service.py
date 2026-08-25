import fitz
from pathlib import Path


class SplitService:

    def __init__(self, pdf_path):

        self.document = fitz.open(pdf_path)

    def split(self, pages_per_request, output_folder):

        output_folder = Path(output_folder)

        output_folder.mkdir(
            exist_ok=True,
            parents=True
        )

        total_pages = len(self.document)

        current = 0

        request_number = 1

        while current < total_pages:

            new_pdf = fitz.open()

            for page_index in range(
                current,
                min(current + pages_per_request, total_pages)
            ):

                new_pdf.insert_pdf(
                    self.document,
                    from_page=page_index,
                    to_page=page_index
                )

            filename = f"request_{request_number}.pdf"

            new_pdf.save(
                output_folder / filename
            )

            new_pdf.close()

            current += pages_per_request

            request_number += 1

        self.document.close()