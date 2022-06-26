import pika
import os
from dotenv import load_dotenv
load_dotenv()
"""
params = pika.URLParameters('amqp://<URL>')

connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=body, properties=properties)
"""

params = pika.URLParameters(os.getenv('AMPQ_CONNECTION_STRING'))
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue

def publish():
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='Hello CloudAMQP!')

    print(" [x] Sent 'Hello World!'")
    
    #connection.close()