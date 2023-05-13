import pika
from random import randint
from time import sleep


# Random get queue A,B,C
def get_queue():
    queue_num=randint(1,3)
    if(queue_num == 1):
        return "A"
    elif(queue_num == 2):
        return "B"
    else:
        return "C"

## Create a connection and 3 queues to send messages to.
credentials = pika.PlainCredentials('guest','guest')
connection= pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672, credentials= credentials))
channel= connection.channel()
channel.exchange_declare('test', durable=True, exchange_type='topic')
channel.queue_declare(queue= 'A')
channel.queue_bind(exchange='test', queue='A', routing_key='A')
channel.queue_declare(queue= 'B')
channel.queue_bind(exchange='test', queue='B', routing_key='B')
channel.queue_declare(queue= 'C')
channel.queue_bind(exchange='test', queue='C', routing_key='C')


## Send messags to a random Queue at a random interval between 1-5 seconds
count = 0
i = 0
while i == 0:
    queue = get_queue()
    message = f'Message numnber {count} on queue: {queue}'
    print('Sending message[' + message + ']')
    channel.basic_publish(exchange='test', routing_key=queue, body= message)
    sleep(randint(0,2))
    count = count + 1

channel.close()


