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
        words = message.split(' ')
        keyword = words[0]
        print 'trying to import ' + 'slaves.keywords.' + keyword + '.process file'
        loaded_mod = __import__('routing.post.slaves.keywords.' + keyword + '.process', fromlist=['accept'])
        try: 
            endpoint = getattr(loaded_mod, 'accept')
            #async request to our endpoint
            endpoint.delay(data)
            return 'routed to keyword'

        except AttributeError:
            return 'getting method "process" failed'

    except ImportError:
        return 'importing keyword failed'

    return data.get('message_type')
