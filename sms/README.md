pre-run


login to venv: . /usr/bin/
drop firewall
run mongo, rabbit, nginx
run workers: celery -A routing.post.notification worker -Q notification --loglevel=info -n notification1.worker.%h
run wsgi: /home/vagrant/projects/sms/venv/bin/gunicorn --bind 0.0.0.0:6969 wsgi:app --pythonpath /home/vagrant/projects/sms    OR DAEMONIZE IT!
