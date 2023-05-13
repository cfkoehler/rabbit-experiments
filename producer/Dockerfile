FROM python:alpine

COPY rabbitProducer.py /rabbitProducer.py
RUN pip install pika

ENTRYPOINT python /rabbitProducer.py