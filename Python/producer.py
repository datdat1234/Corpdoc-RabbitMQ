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
    amqp_mongo_queue,
)

##################################################################

amqp_url = (
    f"{amqp_protocol}://{amqp_username}:{amqp_password}@{amqp_hostname}/{amqp_vhost}"
)
params = pika.URLParameters(amqp_url)

# Create producer connection
producer_conn = pika.BlockingConnection(params)
producer_channel = producer_conn.channel()

# Initialize the producer channel
producer_channel.queue_declare(queue=amqp_mongo_queue, durable=True)
producer_channel.basic_qos(prefetch_count=10)
producer_channel.basic_publish(
    exchange="",
    routing_key=amqp_mongo_queue,
    body="Hello World!",
    properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
)
producer_conn.close()