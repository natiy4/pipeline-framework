 # Deserialize msgpack-encoded values
import msgpack
from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers=['localhost:29092'],
                        value_deserializer=msgpack.loads)
consumer.subscribe(['yossi'])
for msg in consumer:
    assert isinstance(msg.value, dict)