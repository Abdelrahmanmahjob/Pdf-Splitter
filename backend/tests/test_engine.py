# from app.services.pdf_engine import PDFEngine


# engine = PDFEngine("uploads/document.pdf")

# print(engine.get_total_pages())

# engine.close()

# from app.services.pdf_engine import PDFEngine

# engine = PDFEngine("uploads/document.pdf")

# engine.rotate_all_pages()

# engine.save("output/test.pdf")

# engine.close()
from app.services.pdf_engine import PDFEngine
from app.services.image_service import ImageService

engine = PDFEngine("uploads/document.pdf")

page = engine.document[0]

image = ImageService.page_to_image(page)

image.save("output/page1.png")

engine.close()

print("Done")

header = ImageService.crop_header(image)

header.save("output/header.png")

request = ImageService.crop_request_region(image)

request.save(
    "output/request_region.png"
)
