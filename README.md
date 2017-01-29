slave-api
=========

Chikka API integration but on a queue-based workflow. It runs on python, flask, nginx, gunicorn, rabbitmq, celery & mongodb for database(redis if ram wasn't that expensive =(   ). Test server runs on Vagrant and workers(gunicorn, celery workers) are daemonized via supervisor.

Installation
============
create an ec2 instance<br />
 - on security group, allow http(port 80)<br /><br />

run: source install.sh<br />
re-login<br />
restart nginx<br />
restart supervisor<br />
run celery workers in foreground or daemonize it<br /><br />

workers: <br /><br />
&nbsp;&nbsp;&nbsp;&nbsp;celery -A routing.post.notification worker -Q notification --loglevel=info -n notification1.worker.%h<br />
&nbsp;&nbsp;&nbsp;&nbsp;celery -A routing.post.message worker -Q message --loglevel=info -n message1.worker.%h<br />
&nbsp;&nbsp;&nbsp;&nbsp;celery -A routing.post.message worker -Q message --loglevel=info -n message2.worker.%h<br />
&nbsp;&nbsp;&nbsp;&nbsp;celery -A routing.post.inbound.keywords.bord.process worker -Q bord --loglevel=info -n bord1.worker.%h<br />


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


