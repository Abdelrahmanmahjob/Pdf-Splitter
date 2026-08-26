from fastapi import APIRouter, UploadFile, File
import os
import shutil
from app.services.pdf_service import rotate_pdf

router = APIRouter()


UPLOAD_FOLDER = "/tmp"


@router.post("/process") # upload
async def upload_pdf(file: UploadFile = File(...)):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    upload_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(UPLOAD_FOLDER, f"rotated_{file.filename}")

    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    rotate_pdf(upload_path, output_path)

    return {
        "uploaded": upload_path,
        "rotated": output_path
    }