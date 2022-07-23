import pika


async def Retrive_data_from_rabbit():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        'localhost', 5672, '/', pika.PlainCredentials('guest', 'guest')))
    channel = connection.channel()
    rabbit_queue = channel.queue_declare(
        queue="my_app", durable=True, passive=True)
    queue_size = rabbit_queue.method.message_count
    if queue_size != 0:
        for method_frame, properties, body in channel.consume('my_app'):

            # Display the message body
            print(body)

            # remove the message from the queue
            await channel.basic_ack(method_frame.delivery_tag)
            clone = clone+body

            # breake in case the queue is fully empty
            if method_frame.delivery_tag == queue_size:
                break


# Close the channel and the connection

    channel.close()
    connection.close()
# instead of the static message in the return we most return the concatination of the body ( queue nodes)
# to send it via email
    return("this method should return the data retrived from rabbitmq ")
