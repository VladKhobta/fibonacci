import functools
from fibonacci import fibonacci

import pika


QUEUE_NAME = 'fibonacci'


class PikaConsumer:
    def __init__(self):
        self.callback_queue = QUEUE_NAME
        self.response = None

    def consume(self):
        credentials = pika.PlainCredentials('guest', 'guest')
        parameters = pika.ConnectionParameters('rabbitmq', credentials=credentials)
        connection = pika.BlockingConnection(parameters)
        #
        # connection = await connect_robust(
        #     host='rabbitmq',
        #     port=5672,
        #     loop=loop
        # )
        channel = connection.channel()
        channel.basic_qos(prefetch_count=100)

        channel.queue_declare(queue=QUEUE_NAME)
        on_message_callback = functools.partial(
            self.on_message, userdata='on_message_userdata')
        channel.basic_consume(QUEUE_NAME, on_message_callback)

        channel.start_consuming()
        print('Message is incoming.')
        connection.close()

    def on_message(self, chan, method_frame, header_frame, body, userdata=None):
        """Called when a message is received. Log message and ack it."""
        print(fibonacci(body['number']))
        chan.basic_ack(delivery_tag=method_frame.delivery_tag)


if __name__ == "__main__":
    consumer = PikaConsumer()
    consumer.consume()
