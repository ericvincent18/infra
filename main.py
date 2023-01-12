import pika
import time
import pandas as pd
import json
from app.models.reviews import Wine

connection = pika.BlockingConnection(pika.ConnectionParameters(host="127.0.0.1"))
time.sleep(10)
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)
print(" [*] Waiting for messages. To exit press CTRL+C")


def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag=method.delivery_tag)


method_frame, header_frame, body = channel.basic_get("task_queue")
if method_frame:
    channel.basic_ack(method_frame.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="task_queue", on_message_callback=callback)
res_dict = json.loads(body.decode("utf-8"))
df = pd.DataFrame(res_dict)

a = 1
# TODO Dataframe function 
# TODO Logger
# TODO Save to db -- delete previously submitted rows
# TODO deployments
# TODO full update of readme
# TODO unlimited description limit
# TODO configs + hide secrets
# TODO update requirements .txt
# TODO  handle initial migration with docker / k8s



