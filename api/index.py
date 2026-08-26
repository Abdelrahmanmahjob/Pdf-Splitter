import sys
import os

# إضافة مجلد الباك إند إلى المسارات ليتمكن Python من قراءة الملفات
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

# استيراد تطبيق fastapi من ملف main.py
from backend.main import app