import fitz
from PIL import Image
import io
from ..core.config import HEADER_HEIGHT_PERCENT, PDF_RENDER_ZOOM , REQUEST_REGION, CODE_REGION

class ImageService:

    @staticmethod
    def page_to_image(page, rotation=0):

        matrix = fitz.Matrix(PDF_RENDER_ZOOM, PDF_RENDER_ZOOM)

        pix = page.get_pixmap(matrix=matrix)

        image = Image.open(io.BytesIO(pix.tobytes("png")))

        if rotation:
            image = image.rotate(rotation, expand=True)

        return image
        
    @staticmethod
    def crop_header(image):

        width, height = image.size

        return image.crop(
            (
                0,
                0,
                width,
                int(height * HEADER_HEIGHT_PERCENT)
            )
        )
    @staticmethod
    def crop_request_region(image):

        return image.crop(
            (

                REQUEST_REGION["left"],

                REQUEST_REGION["top"],

                REQUEST_REGION["right"],

                REQUEST_REGION["bottom"]

            )
        )

    @staticmethod
    def crop_code_region(image):

        return image.crop(

            (

                CODE_REGION["left"],

                CODE_REGION["top"],

                CODE_REGION["right"],

                CODE_REGION["bottom"]

            )
        )
    