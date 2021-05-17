# amqps://dasyznpw:***@hippo.rmq2.cloudamqp.com/dasyznpw
import pika, json

params = pika.URLParameters('amqps://dasyznpw:gbFu0tHaWPlVijHSH6KT0Y7p5TndLZes@hippo.rmq2.cloudamqp.com/dasyznpw')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)