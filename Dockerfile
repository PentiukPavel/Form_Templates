FROM python:3.12-slim

ENV AUTH_SECRET secret_key
ENV ERROR_LOG_FILENAME errors.json

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -U pip && \
    pip3 install -r /app/requirements.txt --no-cache-dir

COPY ./src /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
