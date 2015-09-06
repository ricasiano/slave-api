# Outbound Message
# this is where we will curl our sms gateway
#
# Author: Rai Icasiano <ricasiano at gmail dot com>
from celery import Celery
from configs.chikka import chikka_config
import requests
import uuid

app = Celery('outbound', backend='amqp://localhost/', broker='amqp://localhost/')
app.config_from_object('slaves.outbound_config.outbound')

@app.task
def accept(mobile_number, request_id, reply):
    config = chikka_config()
    message_id = str(uuid.uuid4())
    values = {
        'message_type' : config['message_type'],
        'mobile_number' : mobile_number,
        'shortcode' : config['shortcode'],
        'request_id' : request_id,
        'message_id' : message_id.replace('-', ''),
        'message' : reply,
        'request_cost' : config['request_cost'],
        'client_id' : config['client_id'],
        'secret_key' : config['secret_key']
    }
    response = requests.post(config['url'], data=values)
    print response.text
