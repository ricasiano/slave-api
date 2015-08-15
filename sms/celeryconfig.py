CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Asia/Manila'
CELERY_ENABLE_UTC = True
CELERY_ROUTES = {
	'slaves.message.accept': {
		'queue': 'message'
	},
	'slaves.notification.accept': {
		'queue': 'notification'
	}
}
