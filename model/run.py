import json
import pika
from app.src.pipeline import Pipeline
from custom_logger import logger

class ModelQHandler:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='provided_data_queue')

    def predict(self, inp):
        pipe = Pipeline(input=inp)
        return pipe.run()

    def on_request(self, ch, method, props, body):
        body = json.loads(body)
        logger.debug(f" [.] provider gets {body}")
        response = self.predict(body)

        self.channel.basic_publish(exchange='',
                                    routing_key=props.reply_to,
                                    properties=pika.BasicProperties(correlation_id=props.correlation_id),
                                    body=json.dumps(response))
        self.channel.basic_ack(delivery_tag=method.delivery_tag)

    def start_consuming(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue='provided_data_queue', on_message_callback=self.on_request)
        logger.debug(" [x] Awaiting provided data of requests")
        self.channel.start_consuming()

if __name__ == "__main__":
    q_handler = ModelQHandler()
    q_handler.start_consuming()