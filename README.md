slave-api
=========

Chikka API integration but on a queue-based workflow. It runs on python, flask, nginx, gunicorn, rabbitmq, celery & mongodb for database(redis if ram wasn't that expensive =(   ). Test server runs on Vagrant and workers(gunicorn, celery workers) are daemonized via supervisor.

Platform Structure:
===================
.
sms/
+--&nbsp;&nbsp;&nbsp;&nbsp;wsgi.py&nbsp;&nbsp;(gunicorn container)<br />
+--&nbsp;&nbsp;&nbsp;&nbsp;api.py&nbsp;&nbsp;(entrypoint once nginx relayed the request, routes wether to go to)<br />
+--&nbsp;&nbsp;&nbsp;&nbsp;celeryconfig.py&nbsp;&nbsp;(configurations as well as routings for workers)<br />
+--&nbsp;&nbsp;&nbsp;&nbsp;mongo.py&nbsp;&nbsp;(mongo connection handler)<br />
+--&nbsp;&nbsp;&nbsp;&nbsp;slaves/<br />
|&nbsp;&nbsp;&nbsp;&nbsp;+--&nbsp;&nbsp;message.py (resource handler for chikka's message inbound transaction)<br />
|&nbsp;&nbsp;&nbsp;&nbsp;+--&nbsp;&nbsp;notification.py (resource handler for chikka's delivery notification)<br />
|&nbsp;&nbsp;&nbsp;&nbsp;+--&nbsp;&nbsp;reply.py (worker for handling message replies for inbound messages)<br />
|&nbsp;&nbsp;&nbsp;&nbsp;+--&nbsp;&nbsp;broadcast.py (**todo** for message broadcasts)<br />
|&nbsp;&nbsp;&nbsp;&nbsp;+--&nbsp;&nbsp;keywords/<br />
|&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;+--&nbsp;&nbsp;project1<br />
|&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;+--&nbsp;&nbsp;project2<br />
|&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;+--&nbsp;&nbsp;projectN<br />
