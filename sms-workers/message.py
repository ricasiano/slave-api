#!/usr/bin/env python
import pika
import logging
logging.basicConfig()

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

#channel.queue_declare(queue='add')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,
                      queue='message',
                      no_ack=True)

channel.start_consuming()
