import json
import pika
from custom_logger import logger
from data_reader.mongo_reader import MongoReader

class DataProviderQHandler:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='request_body_queue')
        self.reader = MongoReader()

    def on_request(self, ch, method, props, body):
        ch.queue_declare(queue='provided_data_queue')
        body = json.loads(body)
        logger.debug(f" [.] provider gets {body}")
        body['dfa'], body['dfb'] = self.reader.read_data_from_mongo(body['uid'], body['book_list'])

        ch.basic_publish(exchange='',
                         routing_key='provided_data_queue',
                         properties=pika.BasicProperties(
                             reply_to=props.reply_to,
                             correlation_id=props.correlation_id,
                         ),
                         body=json.dumps(body))
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start_consuming(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue='request_body_queue', on_message_callback=self.on_request)
        logger.debug(" [x] Awaiting body of requests")
        self.channel.start_consuming()

if __name__ == "__main__":
    q_handler = DataProviderQHandler()
    q_handler.start_consuming()