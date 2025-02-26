import json
from os import getenv

from confluent_kafka import Consumer

from application.port.inbound.event_handler import EventHandler
from domain.event_info import EventInfo

KAFKA_SERVER_ADDRESS = getenv("KAFKA_SERVER_ADDRESS", "localhost:9092")
KAFKA_CONSUMER_GROUP_NAME = getenv("KAFKA_CONSUMER_GROUP_NAME", "consumer_group_1")
KAFKA_OFFSET_MODE = getenv("KAFKA_OFFSET_MODE", "earliest")
TOPIC_NAME = getenv("TOPIC_NAME", "incident_topic")

CONF = {
    'bootstrap.servers': KAFKA_SERVER_ADDRESS,
    'group.id': KAFKA_CONSUMER_GROUP_NAME,
    'auto.offset.reset': KAFKA_OFFSET_MODE
}


class KafkaEventHandler(EventHandler):

    def __init__(self):
        self.kafka_consumer = self.__crate_consumer()

    def handle_event(self) -> EventInfo:
        msg = self.kafka_consumer.poll(1.0)

        if msg is None or msg.error():
            return None

        message_value = msg.value().decode('utf-8')
        print(f"KAFKA MSG {message_value}")
        self.kafka_consumer.commit()
        return EventInfo.of(json.loads(message_value))

    def __crate_consumer(self) -> Consumer:
        consumer = Consumer(CONF)
        consumer.subscribe([TOPIC_NAME])
        return consumer
