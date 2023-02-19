FROM python:3.10-slim

COPY . /consumer
WORKDIR /consumer

RUN pip install pika

CMD ["python", "consumer.py"]