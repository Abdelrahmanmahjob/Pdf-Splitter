import sys
import os

# إضافة مجلد backend للمسارات
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

# استيراد app مباشرة من main.py
from main import app