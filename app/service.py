import pika
import time
import json
from sql.process_data import dataProcessing
import logging
from celery import bootsteps
# from config.env_config import config
from kombu import Queue, Exchange, Consumer

review_queue = Queue(
    "reviews.trigger",
    Exchange("wine.topics", "topic"),
    routing_key="wine.reviews.from.consumer",
)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="rabbitmq",
        port=5672,
        credentials=pika.PlainCredentials("user", "pass"),
    )
)
logging.info("we are connected")
time.sleep(2)
channel = connection.channel()

channel.queue_declare(queue="wine.reviews.from.consumer", durable=True)
logging.info("succesfully connected")


class MsgConsumerStep(bootsteps.ConsumerStep):
    def get_consumers(self, channel):
        return [
            Consumer(
                channel,
                queues=review_queue,
                callbacks=[self.get_message],
                accept=["json", "application"],
            )
        ]

    def get_message(self, body, message):
        body = json.loads(body)
        message.ack()
        message_type = self._get_message_type(message)
        if message_type in ["reviews_received"]:
            try:
                df = dataProcessing(body)
                df.formatDf()
                df.insert_data()

            except:
                logging.warning("error processing body")

    def _get_message_type(self, message):
        if message.delivery_info["routing_key"] == "wine.reviews.from.consumer":
            message_type = "reviews_received"
        return message_type