from celery import Celery

from configs.mongo import mongo_collections
import time

collections = mongo_collections()
subscribers = collections.subscribers

app = Celery('notification', backend='amqp://localhost/', broker='amqp://localhost/')
app.config_from_object('configs.celery')

@app.task
def accept(data, path):
    time.sleep(3)
    subscribers.insert_one({'msisdn': '639171111111', 'subscriptions': [{'tts': {'messages':[{'message': data.get('message')}]}}]})
    return data.get('message_type')
