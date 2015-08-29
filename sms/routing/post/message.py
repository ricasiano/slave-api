from celery import Celery
from mongo import mongo_collections
collections = mongo_collections()
subscribers = collections.subscribers

app = Celery('message', backend='amqp://localhost/', broker='amqp://localhost/')
app.config_from_object('celeryconfig')

@app.task
def accept(data, path):
    #requeue based on keyword, so it will be on a per-project basis. there will also be
    #a catch all for invalid/error keywords
    return data.get('message_type')