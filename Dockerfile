FROM python:3.10

WORKDIR /app

COPY src /app/src
COPY models /app/models
COPY requirements.txt /app

EXPOSE 80

RUN pip install -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
