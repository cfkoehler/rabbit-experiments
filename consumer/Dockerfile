FROM python:alpine

COPY rabbitConsumer.py /rabbitConsumer.py
RUN pip install pika

ENTRYPOINT python /rabbitConsumer.py