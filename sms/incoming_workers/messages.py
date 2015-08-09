from celery import Celery

app = Celery('messages', backend='amqp://localhost/', broker='amqp://localhost/')
app.config_from_object('celeryconfig')
@app.task
def add(x, y):
    return x + y
