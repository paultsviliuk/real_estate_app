import pika, json


params = pika.URLParameters('{{Your_AMQP_URL}}')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='core', body=json.dumps(body), properties=properties)
