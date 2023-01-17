import pika
import time
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost:15672"))
time.sleep(2)
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)
print(" [*] Waiting for messages. To exit press CTRL+C")


def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    method_frame, header_frame, body = channel.basic_get("task_queue")
    if method_frame:
        channel.basic_ack(method_frame.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="task_queue", on_message_callback=callback)
    res_dict = json.loads(body.decode("utf-8"))

    from sql.process_data import initSession, dataProcessing

    df = dataProcessing(res_dict)
    df.formatDf()
    df.insert_data()


if __name__ == "__main__":
    main()
