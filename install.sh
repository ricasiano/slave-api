#!/bin/sh
sudo cat <<EOF > sudo /etc/apt/sources.list.d/rabbitmq.list
sudo deb http://www.rabbitmq.com/debian/ testing main
EOF

sudo curl https://www.rabbitmq.com/rabbitmq-release-signing-key.asc -o /tmp/rabbitmq-release-signing-key.asc
sudo apt-key add /tmp/rabbitmq-release-signing-key.asc
sudo rm /tmp/rabbitmq-release-signing-key.asc

sudo apt-get -qy update
sudo apt-get -qy install rabbitmq-server
sudo apt-get -qy install nginx supervisor python-pip mongodb

echo "[program:sms]
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
directory=/home/ubuntu/apps/slave-api" | sudo tee --append /etc/supervisor/conf.d/pycon.conf > /dev/null

echo "server {
    listen 0.0.0.0:80;
    server_name *.amazonaws.com;
    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/apps/slave-api/app.sock;
    }
}" | sudo tee --append /etc/nginx/conf.d/default.conf > /dev/null
pip install --upgrade pip
sudo pip install virtualenv
mkdir apps
cd apps
git clone https://github.com/ricasiano/slave-api.git
cd slave-api/sms
virtualenv venv
. venv/bin/activate
pip install flask
pip install celery
pip install pymongo
pip install gunicorn
pip install pika
echo "CHIKKA_CLIENT_ID=\"YOUR_CHIKKA_CLIENT_ID\"
CHIKKA_SECRET_KEY=\"YOUR_CHIKKA_SECRET_KEY\"
CHIKKA_SHORTCODE=YOUR_SHORTCODE_HERE" >> /home/ubuntu/.profile
exit
