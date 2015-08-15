slave-api
=========

Chikka API integration but on a queue-based workflow. It runs on python, flask, nginx, gunicorn, rabbitmq, celery & mongodb for database(redis if ram wasn't that expensive =(   ). Test server runs on Vagrant and workers(gunicorn, celery workers) are daemonized via supervisor.

Platform Structure:
===================

sms/
--> wsgi.py (gunicorn container)
--> api.py  (entrypoint once nginx relayed the request, routes wether to go to )
--> celeryconfig.py (configurations as well as routings for workers)
--> mongo.py (mongo connection handler)
--> slaves/
  |--> message.py (resource handler for chikka's message inbound transaction)
  |--> notification.py (resource handler for chikka's delivery notification)
  |--> reply.py (worker for handling message replies for inbound messages)
  |--> broadcast.py (**todo** for message broadcasts)
  |--> keywords/
     |-->project1
     |-->project2
     |-->projectN
