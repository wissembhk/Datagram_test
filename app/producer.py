from datetime import datetime
import pika


def push_to_rabbitmq(tablename: str):
    now = datetime.now()
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        'localhost', 5672, '/', pika.PlainCredentials('guest', 'guest')))
    channel = connection.channel()

    channel.basic_publish(exchange='myexchange', routing_key='test',
                          body="method add executed on table "+tablename+" at "+now.strftime("%H:%M:%S"))
    connection.close()
