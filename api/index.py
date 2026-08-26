import sys
import os

# إضافة مجلد الباك إند للمسارات
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

from main import app

# لضمان عدم تكرار البادئة في مسارات FastAPI
app.root_path = ""