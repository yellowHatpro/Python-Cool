#!/usr/bin/env python
import pika

#connection with the broker 
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#creating a queue, named hello
channel.queue_declare(queue='hello')

#Sending a message to the hello queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

#closing connection
connection.close()
