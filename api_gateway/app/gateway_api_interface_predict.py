import time

import flask
from flask_restful import Resource, request
from schema import Schema, And, Use

from custom_logger import logger
from app.gateway_msg_broker import GatewayMsgBroker

input_schema = Schema({'uid': And(Use(int), lambda n: 0 < n),
                       'book_list': [And(Use(int), lambda n: 0 < n)]})


def validate(data):
    try:
        return input_schema.validate(data), None
    except:
        return None, {"msg": "invalid input", "status": 400}


def generate_ouput(result, errors, elapsed_time):
    output = {"result": {}, "error": {}, "meta": {}, "status": 200}
    if result:
        output["result"] = result
        output["meta"]["elapsed_time(s)"] = elapsed_time
    if errors:
        output["error"] = errors["msg"]
        if "status" in errors:
            output["status"] = errors["status"]
    return output


class ApiInterfacePredict(Resource):
    def post(self):
        try:
            result = None
            data, errors = validate(request.json)
            started_time = time.time()
            if data:
                input = data
                prediction_rpc = GatewayMsgBroker()
                logger.debug(f" [x] Requesting predict of {input}")
                result = prediction_rpc.call(input)
            elapsed_time = time.time() - started_time
            response = generate_ouput(result, errors, elapsed_time)
            return response
        except Exception as e:
            logger.error(f" flask error: {e}")
            flask.abort(500)
