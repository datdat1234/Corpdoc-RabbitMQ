######################### LIBRARY ################################

import pika

##################################################################

#######################   VARIABLE   #############################

from envLoader import (
    amqp_protocol,
    amqp_username,
    amqp_password,
    amqp_hostname,
    amqp_vhost,
    amqp_langchain_queue,
)

##################################################################

amqp_url = (
    f"{amqp_protocol}://{amqp_username}:{amqp_password}@{amqp_hostname}/{amqp_vhost}"
)
params = pika.URLParameters(amqp_url)

# Consumer connection
consumer_conn = pika.BlockingConnection(params)
consumer_channel = consumer_conn.channel()

consumer_channel.queue_declare(queue=amqp_langchain_queue, durable=True)


def callback(ch, method, properties, body):
    req = body.decode("utf-8")
    print(req)


consumer_channel.basic_consume(amqp_langchain_queue, callback, auto_ack=True)
consumer_channel.start_consuming()