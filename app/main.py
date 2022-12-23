import pika
import time
import pandas as pd
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host="127.0.0.1"))
time.sleep(10)
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)
print(" [*] Waiting for messages. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b"."))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

# channel.start_consuming()
method_frame, header_frame, body = channel.basic_get('task_queue')
if method_frame:
    print(method_frame, header_frame, body)
    channel.basic_ack(method_frame.delivery_tag)
else:
    print('No message returned')



channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="task_queue", on_message_callback=callback)

to_db = pd.DataFrame(body)
