import pika
import os
import json
from sender import FibSender



# QUEUE_NAME = os.environ.get('QUEUE_NAME')
# PORT = int(os.environ.get('PORT'))


def fibonacci(n):
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)





if __name__ == "__main__":
    FibSender.send(10)
    FibSender.send(100)
    FibSender.send(56)
    print("Done.")
