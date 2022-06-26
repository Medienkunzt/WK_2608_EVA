import pika
from app import app
from routes import *
import os
from dotenv import load_dotenv
load_dotenv()

"""
params = pika.URLParameters('amqp://<URL>')

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Message received')

    if properties.content_type == 'project_created':
        print('Project got created')
        return redirect(url_for('index'))

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
channel.close()
"""

params = pika.URLParameters(os.getenv('AMPQ_CONNECTION_STRING'))
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue

def callback(ch, method, properties, body):
    print(" [x] Received " + str(body))

channel.basic_consume('hello',
                      callback,
                      auto_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
#connection.close()