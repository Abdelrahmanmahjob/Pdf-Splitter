import sys
import os
import uvicorn

# إضافة مجلد backend للمسارات
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

from main import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)