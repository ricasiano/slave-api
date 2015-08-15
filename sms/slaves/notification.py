from celery import Celery
import time
from mongo import mongoCollections
collections = mongoCollections()
subscribers = collections.subscribers

app = Celery('notification', backend='amqp://localhost/', broker='amqp://localhost/')
app.config_from_object('celeryconfig')

@app.task
def accept(data):
    time.sleep(3)
    subscribers.insert_one({'msisdn': '639171111111', 'subscriptions': [{'tts': {'messages':[{'message': data.get('message')}]}}]})
    return data.get('message_type')
