import sys
import os
import gradio as gr

# إضافة مجلد backend إلى مسارات النظام
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

from main import app as fastapi_app

# إنشاء واجهة Gradio بسيطة وتمرير تطبيق FastAPI إليها
demo = gr.Interface(fn=lambda x: x, inputs="text", outputs="text")
app = gr.mount_gradio_app(fastapi_app, demo, path="/ui")

if __name__ == "__main__":
    # تشغيل عبر demo.launch بدلاً من uvicorn.run لضمان استمرار السيرفر
    demo.launch(server_name="0.0.0.0", server_port=7860)