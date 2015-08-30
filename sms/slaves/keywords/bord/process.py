# some_file.py
from celery import Celery
from configs.mongo import mongo_collections
collections = mongo_collections()
subscribers = collections.subscribers

app = Celery('bord', backend='amqp://localhost/', broker='amqp://localhost/')
app.config_from_object('slaves.keywords.bord.config.celery')

@app.task
def accept(data):
    print 'reached keyword, now processing the parameters'
    return 'success processing'
