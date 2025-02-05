import pika, json

from core import House, db


amqp_url = "amqps://mtvqdhex:hITzepEi6xooDvcF3i2pnf6qqdfdwalJ@rattlesnake.rmq.cloudamqp.com/mtvqdhex"
params = pika.URLParameters(amqp_url)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='core')


def callback(ch, method, properties, body):
    print('Received in core')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'house_created':
        house = House(id=data['id'], name=data['name'], image=data['image'], description=data['description'])
        db.session.add(house)
        db.session.commit()
        print('House Created')

    elif properties.content_type == 'house_updated':
        house = House.query.get(data['id'])
        house.name = data['name']
        house.image = data['image']
        house.description = data['description']
        db.session.commit()
        print('House Updated')

    elif properties.content_type == 'product_deleted':
        house = House.query.get(data)
        db.session.delete(house)
        db.session.commit()
        print('House Deleted')


channel.basic_consume(queue='core', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
