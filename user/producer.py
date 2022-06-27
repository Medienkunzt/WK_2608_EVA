import json
import pika, os
from dotenv import load_dotenv
load_dotenv()

params = pika.URLParameters(os.getenv('AMPQ_CONNECTION_STRING'))

connection = pika.BlockingConnection(params)

channel = connection.channel() # start a channel

channel.queue_declare(queue='likeProject') # Declare a queue

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='',
                        routing_key='likeProject',
                        body=json.dumps(body),
                        properties=properties)

    print(" [x] Sent like")
    
    #connection.close()