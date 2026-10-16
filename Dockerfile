FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY scikit_demo.py .

CMD ["python", "-u", "scikit_demo.py"]
