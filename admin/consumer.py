import pika, os, json
from app import *
import db
from dotenv import load_dotenv
load_dotenv()

params = pika.URLParameters(os.getenv('AMPQ_CONNECTION_STRING'))
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='likeProject') # Declare a queue

def callback(ch, method, properties, body):
    print(" [x] Received " + str(properties.content_type) + str(json.loads(body)))
    db.increment_likes(int(json.loads(body)))

channel.basic_consume(queue='likeProject',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()

#channel.close()
#connection.close()