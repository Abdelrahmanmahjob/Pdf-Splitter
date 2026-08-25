import fitz
import os


def rotate_pdf(input_path: str, output_path: str):

    document = fitz.open(input_path)

    for page in document:

        page.set_rotation(-270)

    document.save(output_path)
    document.close()