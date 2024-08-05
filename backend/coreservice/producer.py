import pika, json


amqp_url = "amqps://mtvqdhex:hITzepEi6xooDvcF3i2pnf6qqdfdwalJ@rattlesnake.rmq.cloudamqp.com/mtvqdhex"
params = pika.URLParameters(amqp_url)

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='config', body=json.dumps(body), properties=properties)
