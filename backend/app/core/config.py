from pathlib import Path

# ==============================
# Project Directories
# ==============================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

UPLOAD_DIR = BASE_DIR / "uploads"

OUTPUT_DIR = BASE_DIR / "output"

TEMP_DIR = BASE_DIR / "temp"


# ==============================
# PDF Settings
# ==============================

PDF_ROTATION = -270

PDF_RENDER_ZOOM = 3


# ==============================
# Crop Settings
# ==============================

HEADER_HEIGHT_PERCENT = 0.18


# ==============================
# OCR Regions
# ==============================

REQUEST_REGION = {

    "left": 1050,

    "top": 0, # 175

    "right": 1450,

    "bottom": 350

}


CODE_REGION = {

    "left": 1250,

    "top": 1330,

    "right": 1600,

    "bottom": 1470

}