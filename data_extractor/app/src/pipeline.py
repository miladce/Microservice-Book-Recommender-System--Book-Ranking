from time import sleep

from app.src.extractor.file_reader import FileReader
from app.src.loader.mongo_loader import MongoLoader
from app.src.validator.action_validator import ActionValidator
from config import data_path
from custom_logger import logger


class Pipeline:

    def __init__(self, strategy=None):
        self.set_default_strategy()
        self.parse_strategy(strategy)

    def parse_strategy(self, strategy: dict = None):
        if strategy:
            if strategy['extractor_type']:
                self.extractor = strategy['extractor_type']
            if strategy['validator_type']:
                self.validator = strategy['validator_type']
            if strategy['loader_type']:
                self.loader = strategy['loader_type']

    def set_default_strategy(self):
        self.extractor = FileReader('dummy.csv', chunksize=2)
        self.validator = ActionValidator()
        self.loader = MongoLoader(target='dummy_actions')

    def run(self, checkpoint_file):

        try:
            with open(f'{data_path}{checkpoint_file}', 'r') as f:
                chkpoint = int(f.read())
        except:
            chkpoint = 0

        while (True):

            with open(f'{data_path}{checkpoint_file}', 'w') as f:
                f.write(str(chkpoint))

            df = self.extractor.read_data(chkpoint)
            if (df is None):
                break
            if len(df)==0:
                break

            validated_df = self.validator.validate_data(df)
            if validated_df is None:
                break

            self.loader.load_data(validated_df)

            chkpoint += len(validated_df)

            logger.debug(f'{chkpoint} numebr of rows inserted')
