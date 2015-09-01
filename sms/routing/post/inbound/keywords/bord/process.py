# Bord! Text to see your message on screen!
# Entrypoint for the bord project. 
#
# Author: Rai Icasiano <ricasiano at gmail dot com>

from celery import Celery
from configs.mongo import mongo_collections
import pika
import json
import uuid
import datetime

collections = mongo_collections()
subscribers = collections.subscribers

app = Celery('bord', backend='amqp://localhost/', broker='amqp://localhost/')
app.config_from_object('routing.post.inbound.keywords.bord.config.celery')

@app.task
def accept(data, keyword, param):
    from routing.post.inbound.keywords.bord.param_factory import ParamFactory
    param_obj = ParamFactory(keyword, param)
    project = param_obj.create()
    projectInstance = project()
    reply = projectInstance.process(data)
    send_message(reply)

def send_message(reply):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
    properties = pika.BasicProperties(content_type='application/json', 
            content_encoding='UTF-8',
            delivery_mode=1)
    channel = connection.channel()
    guid = uuid.uuid4()
    message = {"id": str(guid),
             "task": "slaves.outbound.accept",
             "body": reply
             "args": [],
             "kwargs": {},
             "retries": 0,
             "eta": datetime.datetime.now().isoformat('T')}
    channel.queue_declare(queue='outbound', durable=True)
    channel.basic_publish(exchange='',
        routing_key='outbound',
        body=json.dumps(message), properties=properties)
    connection.close()
