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
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://pdf-splitter-coral-eight.vercel.app",
    ],
    # السماح بكل دومينات vercel الفرعية الخاصة بمشروعك بشكل ديناميكي
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(status_router)