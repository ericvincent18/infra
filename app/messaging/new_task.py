import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=15672)
)
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)
with open("/Users/ericvincent/Desktop/winemag-data-130k-v2.json", "r") as read_file:
    f = read_file.read()

message = f
channel.basic_publish(
    exchange="",
    routing_key="task_queue",
    body=message,
    properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE),
)

connection.close()
