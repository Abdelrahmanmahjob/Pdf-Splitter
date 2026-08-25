from fastapi import APIRouter
from app.core.job_status import job_status

router = APIRouter()

@router.get("/status")
def get_status():
    return job_status