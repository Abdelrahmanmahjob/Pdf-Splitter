FROM python:3.10-slim

# تثبيت مكتبات النظام المطلوبة لـ PyMuPDF و OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . /code

EXPOSE 7860

CMD ["python", "server.py"]