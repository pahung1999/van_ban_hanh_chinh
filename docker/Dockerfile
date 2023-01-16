FROM python:3.9-slim-bullseye

RUN apt-get update
RUN apt-get install -y poppler-utils tesseract-ocr-vie

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip cache purge
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
