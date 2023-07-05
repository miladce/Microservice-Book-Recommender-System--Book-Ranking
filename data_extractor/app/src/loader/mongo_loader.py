from time import sleep

from app.src.loader.data_loader import DataLoader
from config import mongo
from custom_logger import logger
import pymongo


class MongoLoader(DataLoader):

    def __init__(self, target):
        cli = pymongo.MongoClient(mongo["host"])
        db_name = mongo["db_name"]
        self.db = cli[db_name]
        self.target_collection_name = target

    def load_data(self, json_data):
        target_collection = self.db[self.target_collection_name]
        success = 0
        for n_try in range(3):
            try:
                target_collection.insert_many(json_data)
                success = 1
            except Exception as e:
                logger.error(
                    f"error {e} in loading this data {json_data} \n to {self.target_collection_name} collection")
                sleep(2)
        if success == 0:
            raise Exception('db error')
