import pika
import sys
import config
import handler
import nfscopy
import os

print 'IMDS Consumder Module',
print 'by Masoud Mehrabi'

if os.geteuid() != 0:
    print "You must run this as root!"
    exit()

print 'Preparing NFS Mount...'
nfscopy.InitMount()

print 'Connecting to Work Dispatcher...'
connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.RABBITMQ_HOST))
channel = connection.channel()
channel.queue_declare(queue=config.RABBITMQ_TASK_QUEUE_NAME, durable=True)
channel.basic_qos(prefetch_count=config.RABBITMQ_PREFETCH_COUNT)
channel.basic_consume(handler.callback, queue=config.RABBITMQ_TASK_QUEUE_NAME)

print 'Start Consuming...'
channel.start_consuming()
