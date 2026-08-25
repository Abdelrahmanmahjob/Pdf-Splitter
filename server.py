import sys
import os
import uvicorn

# إضافة مجلد backend إلى مسارات النظام
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

from main import app

if __name__ == "__main__":
    # تشغيل تطبيق FastAPI مباشرة على المنفذ المطلوبة من Hugging Face
    uvicorn.run(app, host="0.0.0.0", port=7860)