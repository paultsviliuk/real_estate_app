import pika, os, django, json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

# import models only after calling django.setup()
from houses.models import House


amqp_url = "amqps://mtvqdhex:hITzepEi6xooDvcF3i2pnf6qqdfdwalJ@rattlesnake.rmq.cloudamqp.com/mtvqdhex"
params = pika.URLParameters(amqp_url)

# Create a connection
connection = pika.BlockingConnection(params)

channel = connection.channel()

# Declare a queue channel
channel.queue_declare(queue='config')

# Defining a callback function
def callback(ch, method, properties, body):
    print('Received in config')
    id = json.loads(body)
    print(id)
    
    house = House.objects.get(id=id)
    
    if house.likes:
        house.likes += 1
        house.save()
        print('House likes increased!')
    else:
        house.checks += 1
        house.save()
        print('House checks increased!')

# initiating message consumption
channel.basic_consume(queue='config', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
