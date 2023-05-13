import pika
from random import randint
from time import sleep

def ack_message(channel, delivery_tag):
    if channel.is_open:
        channel.basic_ack(delivery_tag)
    else:
        pass

#defining callback functions responding to corresponding queue callbacks
def callbackFunctionForQueueA(ch,method,properties,body):
 print('Got a message from Queue A: ', body)
 sleep(randint(2,5))
 channel.basic_ack(method.delivery_tag)
 print('Ack message: ', body)
def callbackFunctionForQueueB(ch,method,properties,body):
 print('Got a message from Queue B: ', body)
 sleep(randint(2,5))
 channel.basic_ack(method.delivery_tag)
 print('Ack message: ', body)
def callbackFunctionForQueueC(ch,method,properties,body):
 print('Got a message from Queue C: ', body)
 sleep(randint(2,5))
 channel.basic_ack(method.delivery_tag)
 print('Ack message: ', body)


sleep(60)

 ## Create a connection and 3 queues to send messages to.
credentials = pika.PlainCredentials('guest','guest')
connection= pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672, credentials= credentials))
channel = connection.channel()
channel.exchange_declare('test', durable=True, exchange_type='topic')

 #Attaching consumer callback functions to respective queues that we wrote above
channel.basic_consume(queue='A', on_message_callback=callbackFunctionForQueueA, auto_ack=False)
channel.basic_consume(queue='B', on_message_callback=callbackFunctionForQueueB, auto_ack=True)
channel.basic_consume(queue='C', on_message_callback=callbackFunctionForQueueC, auto_ack=False)
#this will be command for starting the consumer session


try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()