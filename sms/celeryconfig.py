CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Asia/Manila'
CELERY_ENABLE_UTC = True
CELERY_ROUTES = {
	'message.accept': {
		'queue': 'message'
	},
	'adder.accept': {
		'queue': 'adder'
	},
	'notification.accept': {
		'queue': 'notification'
	}
}
