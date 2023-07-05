from flask import Flask
from flask_restful import Api
from app.gateway_api_interface_predict import ApiInterfacePredict

app = Flask(__name__)
api = Api(app)

api.add_resource(ApiInterfacePredict, '/predict')
