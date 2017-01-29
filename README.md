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

1. create ubuntu instance
2. open port 80 from amazon security group
3. get the hostname that we are connecting to: ec2-13-112-67-6.ap-northeast-1.compute.amazonaws.com
4. install rabbitmq: https://www.rabbitmq.com/ec2.html
5. install mongodb
6. install python-pip
7. install from pip:
    - virtualenv
8. create directory 'apps'
9. checkout https://github.com/ricasiano/slave-api.git
10.  go to 'sms' directory
11. enable virtualenv: virtualenv venv
12. run: 'source venv/bin/activate'
13. create the environment variables
    CHIKKA_CLIENT_ID="YOUR CHIKKA ID HERE"
    CHIKKA_SECRET_KEY="YOUR CHIKKA SECRET KEY HERE"
    CHIKKA_SHORTCODE="YOUR SHORTCODE HERE"
14. logout/login again to that session
15. create __init__.py on configs directory

*******************
test: on 'sms' directory
workers: 
    celery -A routing.post.notification worker -Q notification --loglevel=info -n notification1.worker.%h
    celery -A routing.post.message worker -Q message --loglevel=info -n message1.worker.%h
    celery -A routing.post.message worker -Q message --loglevel=info -n message2.worker.%h
    celery -A routing.post.inbound.keywords.bord.process worker -Q bord --loglevel=info -n bord1.worker.%h
*******************

16. Install gunicorn from pip
17. /etc/supervisor/conf.d
*******************

[program:sms]
command=/home/ubuntu/apps/slave-api/sms/venv/bin/gunicorn --bind unix:app.sock api:app --pythonpath /home/ubuntu/apps/slave-api/sms
priority=999                ; the relative start priority (default 999)
autostart=true              ; start at supervisord start (default: true)
autorestart=true            ; retstart at unexpected quit (default: true)
startsecs=10                ; number of secs prog must stay running (def. 10)
startretries=3              ; max # of serial start failures (default 3)
exitcodes=0,2               ; 'expected' exit codes for process (default 0,2)
stopsignal=QUIT             ; signal used to kill process (default TERM)
stopwaitsecs=10             ; max num secs to wait before SIGKILL (default 10)
user=ubuntu                 ; setuid to this UNIX account to run the program
log_stdout=true             ; if true, log program stdout (default true)
log_stderr=true             ; if true, log program stderr (def false)
logfile=/var/log/flask-sms.log    ; child log path, use NONE for none; default AUTO
logfile_maxbytes=1MB        ; max # logfile bytes b4 rotation (default 50MB)
logfile_backups=10          ; # of logfile backups (default 10)
directory=/home/ubuntu/apps/slave-api
*******************

18. install nginx
19. go to /etc/nginx/conf.d/default.conf

*******************
server {
    listen 0.0.0.0:80;
    server_name *.amazonaws.com;
    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/apps/slave-api/app.sock;
    }
}
*******************
