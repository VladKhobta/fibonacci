FROM python:3.10-slim

COPY . /sender
WORKDIR /sender

RUN pip install pika

CMD ["python", "sender.py"]