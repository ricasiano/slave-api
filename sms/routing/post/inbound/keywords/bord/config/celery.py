CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Asia/Manila'
CELERY_IMPORTS =('routing.post.inbound.keywords.bord.process')
CELERY_ENABLE_UTC = True
CELERY_ROUTES = {
    'routing.post.inbound.keywords.bord.process.accept': {
        'queue': 'bord'
    }    
}
