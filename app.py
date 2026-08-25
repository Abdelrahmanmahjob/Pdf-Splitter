import sys
import os

# إضافة مجلد backend إلى مسارات Python لتجنب التضارب مع app.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

import gradio as gr
from main import app as fastapi_app  # الاستيراد المباشر بعد إضافة المجلد إلى sys.path

# دمج FastAPI مع واجهة Gradio
app = gr.mount_gradio_app(fastapi_app, gr.Interface(lambda x: x, "text", "text"), path="/gradio")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)