slave-api
=========

Chikka API integration but on a queue-based workflow. It runs on python, flask, nginx, gunicorn, rabbitmq, celery & mongodb for database(redis if ram wasn't that expensive =(   ). Test server runs on Vagrant and workers(gunicorn, celery workers) are daemonized via supervisor.

Platform Structure:
===================
.
sms/
+-- wsgi.py (gunicorn container)<br />
+-- api.py  (entrypoint once nginx relayed the request, routes wether to go to)<br />
+-- celeryconfig.py (configurations as well as routings for workers)<br />
+-- mongo.py (mongo connection handler)<br />
+-- slaves/<br />
|   +-- message.py (resource handler for chikka's message inbound transaction)<br />
|   +-- notification.py (resource handler for chikka's delivery notification)<br />
|   +-- reply.py (worker for handling message replies for inbound messages)<br />
|   +-- broadcast.py (**todo** for message broadcasts)<br />
|   +-- keywords/<br />
|   |   +--project1<br />
|   |   +--project2<br />
|   |   +--projectN<br />
