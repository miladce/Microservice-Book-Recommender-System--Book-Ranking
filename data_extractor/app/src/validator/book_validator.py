from app.src.validator.data_validator import DataValidator
from schema import Schema, And, Use

from custom_logger import logger


class BookValidator(DataValidator):
    def __init__(self):
        self.schema = Schema([{'book_id': And(Use(int), lambda n: 0 < n)}])

    def validate_data(self, data):

        try:
            data.index = data.index + 1
            data = data.to_dict('records')
            return data
        except Exception as e:
            logger.error(f'data validation error: {e}')
            return None
