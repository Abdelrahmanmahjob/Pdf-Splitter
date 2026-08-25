import asyncio
from starlette.datastructures import UploadFile as StarletteUploadFile
from pathlib import Path
import io

from app.api.routes import process_pdf

async def main():
    pdf_path = Path("uploads/document.pdf")
    if not pdf_path.exists():
        print("PDF not found", pdf_path)
        return

    f = open(pdf_path, "rb")
    upload = StarletteUploadFile(filename=pdf_path.name, file=f)

    # Call the route handler directly
    try:
        resp = await process_pdf(
            pdf=upload,
            pages_per_request=3,
            fixed_code=None,
            pdf_rotation=0,
            ocr_rotation=0,
            auto_rotate=False,
        )
        print("Response type:", type(resp))
        if hasattr(resp, 'media_type'):
            print('media_type:', resp.media_type)
    except Exception as e:
        import traceback

        print("Exception:")
        traceback.print_exc()
    finally:
        f.close()

if __name__ == '__main__':
    asyncio.run(main())
