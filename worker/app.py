import pika
import time

sleepTime = 10
print(f" [*] Sleeping for: {sleepTime} seconds")

time.sleep(30)

print(' [*] Connecting to server...')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='task-queue', durable=True)
print(' [*] Waiting for messagges')

def callback(ch, method, properties, body):
    print(f" [x] Received: {body}")
    cmd = body.decode()

    if cmd == 'hey':
        print('Hey there!')
    elif cmd == 'hello':
        print('Well, hello there')
    else:
        print("Sorry I don't understand :(", body)
    print("[x] Done")

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count = 1)
channel.basic_consume(queue='task-queue', on_message_callback=callback)
channel.start_consuming()