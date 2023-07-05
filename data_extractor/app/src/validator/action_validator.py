from builtins import Exception

from pandas import DataFrame

from app.src.validator.data_validator import DataValidator
from custom_logger import logger
from schema import Schema, And, Use


class ActionValidator(DataValidator):
    def __init__(self):
        self.schema = Schema([{'AccountId': And(Use(int), lambda n: 0 <= n),
                               'book_id': And(Use(int), lambda n: 0 <= n),
                               'CreationDate': And(str, len)}])

    def validate_data(self, data: DataFrame):
        try:
            data.rename(columns={"BookId": "book_id"}, inplace=True)
            data.index = data.index + 1
            data=data.to_dict('records')
            return self.schema.validate(data)
        except Exception as e:
            logger.error(f'data validation error: {e}')
            return None
