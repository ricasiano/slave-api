from celery import Celery
import time
from mongo import mongoCollections
collections = collections()
subscribers = collections.subscribers

app = Celery('message', backend='amqp://localhost/', broker='amqp://localhost/')
app.config_from_object('celeryconfig')

@app.task
def accept(data):
    #requeue based on keyword, so it will be on a per-project basis. there will also be
    #a catch all for invalid/error keywords
    return data.get('message_type')
