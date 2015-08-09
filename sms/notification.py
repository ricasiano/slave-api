from celery import Celery

app = Celery('notification', backend='amqp://localhost/', broker='amqp://localhost/')
#app.config_from_object('celeryconfig')

@app.task
def notification_accept(data):
    return data.get('message_type')
