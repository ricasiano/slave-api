from celery import Celery

app = Celery('messages', broker='amqp://localhost')

@app.task
def add(x, y):
    return x + y
