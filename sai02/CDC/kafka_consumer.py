"""
Consumer
"""
from kafka import KafkaConsumer

def main():
    # Define server with port
    bootstrap_servers = ['localhost:9092']

    # Define topic name from where the message will recieve
    topicName = 'mysql1.inventory.customers'

    # Initialize consumer variable
    consumer = KafkaConsumer(
        topicName,
        bootstrap_servers=bootstrap_servers,
        # value_deserializer=lambda v: json.dumps(v).encode("utf-8")
    )

    for message in consumer:
        print(message.value)

if __name__ == "__main__":
    main()