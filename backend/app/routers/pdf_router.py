from fastapi import APIRouter, UploadFile, File
import os
import shutil
from app.services.pdf_service import rotate_pdf

router = APIRouter()


UPLOAD_FOLDER = "uploads"


@router.post("/process") # upload
async def upload_pdf(file: UploadFile = File(...)):

    upload_path = os.path.join("uploads", file.filename)

    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    output_path = os.path.join(
        "output",
        f"rotated_{file.filename}"
    )

    rotate_pdf(upload_path, output_path)

    return {
        "uploaded": upload_path,
        "rotated": output_path
    }