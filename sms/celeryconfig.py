CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Asia/Manila'
CELERY_ENABLE_UTC = True
CELERY_ROUTES = {
	'routing.post.message.accept': {
		'queue': 'message'
	},
	'routing.post.notification.accept': {
		'queue': 'notification'
	}
}
