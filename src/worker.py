
import json
from kafka import KafkaConsumer, KafkaProducer

consumer = KafkaConsumer(bootstrap_servers='localhost:29092',
                                 auto_offset_reset='earliest',
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))
consumer.subscribe(['MMR'])

while True:
    for message in consumer:
        print (message)