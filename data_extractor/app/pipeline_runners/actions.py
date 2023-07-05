from app.src.extractor.file_reader import FileReader
from app.src.loader.mongo_loader import MongoLoader
from app.src.validator.action_validator import ActionValidator

strategy = {
    'extractor_type': FileReader('actions.csv', chunksize=10 ** 4),
    'validator_type': ActionValidator(),
    'loader_type': MongoLoader(target='actions')
}