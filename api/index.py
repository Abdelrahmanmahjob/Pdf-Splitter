import sys
import os

# إضافة مجلد backend لمسارات النظام
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

from main import app

# مهم جداً: إلغاء الـ root_path إذا كانت المسارات معرفة مباشرة كـ /process و /status
app.root_path = ""