from flask import Flask
import pika

app = Flask(__name__)

@app.route('/')
def index():
    return 'OK'

@app.route('/job/<cmd>')
def add(cmd):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='task-queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='task-queue', 
        body=cmd,
        properties=pika.BasicProperties(
            # Make message persistent
            delivery_mode=2
        ),
    )
    connection.close()
    return f"[x] Sent: {cmd}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')