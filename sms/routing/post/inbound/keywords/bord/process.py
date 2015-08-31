# Bord! Text to see your message on screen!
# Entrypoint for the bord project. 
#
# Author: Rai Icasiano <ricasiano at gmail dot com>

from celery import Celery
from configs.mongo import mongo_collections
import pika

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
    reply = projectInstance.process(data, param.pop(0))
    outbound(reply)

def send_message(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='outbound')
    channel.basic_publish(exchange='',
        routing_key='outbound',
        body=data)
    connection.close()
