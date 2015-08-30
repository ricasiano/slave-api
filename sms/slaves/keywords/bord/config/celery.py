CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Asia/Manila'
CELERY_IMPORTS =('routing.post.slaves.keywords.bord.process')
CELERY_ENABLE_UTC = True
