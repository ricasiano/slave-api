CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Asia/Manila'
CELERY_ENABLE_UTC = True
CELERY_IMPORTS =('slaves.outbound')
CELERY_ROUTES = {
	'slaves.outbound.accept': {
		'queue': 'outbound'
	},
}
