# Bord! Text to see your message on screen!
# Entrypoint for the bord project. 
#
# Author: Rai Icasiano <ricasiano at gmail dot com>

from celery import Celery

app = Celery('outbound', backend='amqp://localhost/', broker='amqp://localhost/')
app.config_from_object('slaves.configs.outbound')

@app.task
def accept():
    print 'asdf';
