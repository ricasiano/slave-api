# Message endpoint, this is where the subscriber's messages
# are handled
#
# Author: Rai Icasiano <ricasiano at gmail dot com>

from celery import Celery
from configs.mongo import mongo_collections
collections = mongo_collections()
subscribers = collections.subscribers

app = Celery('message', backend='amqp://localhost/', broker='amqp://localhost/')
app.config_from_object('configs.celery')

@app.task
def accept(data):
    """
        requeue based on keyword, so it will be on a per-project basis. there will also be
        a catch all for invalid/error keywords
    """
    try:
        #get our keyword, this will be the basis on which project we should be loading 
        message = data.get('message')
        texts = message.split(' ')
        keyword = texts.pop(0).lower()
        param = texts.pop(0).lower()
        loaded_mod = __import__('routing.post.inbound.keywords.' + keyword + '.process', fromlist=['accept'])
        try: 
            project = getattr(loaded_mod, 'accept')
            #async request to our endpoint
            project.delay(data, keyword, param)
            return 'routed to keyword'

        except AttributeError:
            return 'getting method "process" failed'

    except ImportError:
        return 'importing keyword failed'
