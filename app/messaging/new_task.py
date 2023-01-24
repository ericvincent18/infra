import pika
import logging
import time
import socket

socket.gethostbyname("")

parameters = pika.URLParameters("amqp://user:pass@localhost:5672/%2F")

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

with open("/Users/ericvincent/Desktop/winemag-data-130k-v2.json", "r") as read_file:
    f = read_file.read()
    message = f

channel.basic_publish(
    "",
    "wine.reviews.from.consumer",
    message,
    pika.BasicProperties(
        content_type="text/plain", delivery_mode=pika.DeliveryMode.Transient
    ),
)

connection.close()
