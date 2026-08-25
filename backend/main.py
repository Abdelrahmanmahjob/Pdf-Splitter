from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.api.status import router as status_router

app = FastAPI(
    title="Request Splitter API",
    version="1.0.0"
) 

app.add_middleware(
    CORSMiddleware,
    # استخدم "*" للسماح بأي دومين في مرحلة التجربة
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(status_router)