import sys
import os
import uvicorn
import gradio as gr

# إضافة مجلد backend للمسارات
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

from main import app as fastapi_app

# دمج FastAPI مع Gradio لضمان استمرار السيرفر على Hugging Face
demo = gr.Interface(lambda x: x, "text", "text")
app = gr.mount_gradio_app(fastapi_app, demo, path="/ui")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)