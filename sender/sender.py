import pika
import json

QUEUE_NAME = 'fibonacci'


class FibSender:
    def __init__(self):
        pass

    @classmethod
    def send(cls, number):
        try:
            print('Trying connect to RabbitMQ.')
            creds = pika.PlainCredentials('guest', 'guest')
            parameters = pika.ConnectionParameters(
                host='rabbitmq',
                port=5672,
                # virtual_host='/',
                credentials=creds
            )
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()
            channel.queue_declare(queue=QUEUE_NAME)
            message = {'number': number}
            channel.basic_publish(exchange='',
                                  routing_key='fibonacci',
                                  body=json.dumps(message))
        except:
            print('Error detected.')
            return

        print(f"Sent message to {QUEUE_NAME} MQ with {number} number.'")
        connection.close()

        return


if __name__ == "__main__":
    FibSender.send(10)
    FibSender.send(100)
    FibSender.send(56)
    print("Done.")
