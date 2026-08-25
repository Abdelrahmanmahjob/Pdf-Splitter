from fastapi import APIRouter, UploadFile, File, Form
from pathlib import Path
import shutil
from typing import Literal
from app.services.process_engine import ProcessEngine
from starlette.concurrency import run_in_threadpool

router = APIRouter()

UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)

RotationType = Literal[-270, -180, -90, 0, 90, 180, 270, "-270", "-180", "-90", "0", "90", "180", "270"]

@router.post("/process")
async def process_pdf(
    pdf: UploadFile = File(...),
    pages_per_request: int = Form(...),
    fixed_code: str | None = Form(None),
    pdf_rotation: RotationType = Form(0),
    ocr_rotation: RotationType = Form(0),
    auto_rotate: bool = Form(False),
):
    import time

    unique_name = f"{int(time.time())}_{pdf.filename}"
    pdf_path = UPLOAD_FOLDER / unique_name

    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(pdf.file, buffer)

    # Validate file saved correctly
    if pdf_path.stat().st_size == 0:
        return {"error": "Uploaded file is empty"}

    # 🎯 تحويل القيم صراحةً إلى int لتجنب خطأ PyMuPDF
    pdf_rot_int = int(pdf_rotation)
    ocr_rot_int = int(ocr_rotation)

    engine = ProcessEngine()
    try:
        # Run heavy processing in a thread so the event loop can still serve /status
        await run_in_threadpool(
            engine.process,
            str(pdf_path),
            pages_per_request,
            "output/final",
            fixed_code,
            pdf_rot_int,
            ocr_rot_int,
            auto_rotate,
        )
    except Exception as e:
        # Ensure we capture processing errors for debugging in logs
        import traceback, os

        os.makedirs("logs", exist_ok=True)
        with open("logs/process_error.log", "a", encoding="utf-8") as fh:
            fh.write("--- ERROR ---\n")
            fh.write(traceback.format_exc())
            fh.write("\n")

        from fastapi.responses import JSONResponse

        return JSONResponse(status_code=500, content={"error": str(e)})

    zip_path = shutil.make_archive(
        "output/result",
        "zip",
        "output/final"
    )

    from fastapi.responses import FileResponse

    return FileResponse(
        zip_path,
        media_type="application/zip",
        filename="Requests.zip"
    )
    # return {
    #     "success": True,
    #     "message": "Done"
    # }
