import sys
import os

# إضافة مجلد backend إلى مسارات النظام
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

import gradio as gr
from main import app as fastapi_app

# دمج تطبيق FastAPI مع Gradio
demo = gr.Interface(lambda x: x, "text", "text")
app = gr.mount_gradio_app(fastapi_app, demo, path="/gradio")

# تشغيل التطبيق عبر Gradio لمنع السيرفر من الإغلاق
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)