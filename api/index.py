import sys
import os

# إضافة مجلد backend إلى مسارات Python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

from main import app

# معالجة بادئة /api لضمان توجيه Routes لـ FastAPI بدون 404
app.root_path = "/api"