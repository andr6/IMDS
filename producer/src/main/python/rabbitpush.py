import pika
import sys
import config

def Enqueue(message):
    try:
        connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=config.RABBITMQ_HOST))

        channel = connection.channel()
        channel.queue_declare(queue=config.RABBITMQ_TASK_QUEUE_NAME,
                durable=True)

        channel.basic_publish(exchange='',
                      routing_key=config.RABBITMQ_TASK_QUEUE_NAME,
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
        connection.close()
    except:
        print "Exception in rabbitpush: " + sys.exc_info()[0]
