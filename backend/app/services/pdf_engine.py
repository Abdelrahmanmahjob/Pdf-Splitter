import fitz
from pathlib import Path
from ..core.config import PDF_ROTATION


class PDFEngine:

    def __init__(self, pdf_path: str):

        self.pdf_path = Path(pdf_path)

        self.document = fitz.open(pdf_path)

        self.total_pages = len(self.document)


    def get_total_pages(self):

        return self.total_pages


    def close(self):

        self.document.close()

    def rotate_all_pages(self):

        for page in self.document:

            page.set_rotation(PDF_ROTATION)

    def save(self, output_path):

        self.document.save(output_path)