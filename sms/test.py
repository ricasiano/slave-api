import os
import random
import time
from flask import Flask, request, render_template, session, flash, redirect, \
    url_for, jsonify
from flask.ext.mail import Mail, Message
from celery import Celery
app = Flask(__name__)

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'amqp://localhost'
app.config['CELERY_RESULT_BACKEND'] = 'amqp://localhost'

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def send_async_email(a, b):
    """Background task to send an email with Flask-Mail."""
    return a+b

@app.route('/', methods=['POST'])
def index():
    send_async_email.delay(1, 2)
    return 202

if __name__ == '__main__':
    app.run(debug=True)

