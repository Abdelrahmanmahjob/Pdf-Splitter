import sys
import os

# إضافة مجلد backend لمسارات النظام
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

import gradio as gr
from backend.main import app as fastapi_app

# دمج FastAPI مع Gradio
app = gr.mount_gradio_app(fastapi_app, gr.Interface(lambda x: x, "text", "text"), path="/gradio")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)