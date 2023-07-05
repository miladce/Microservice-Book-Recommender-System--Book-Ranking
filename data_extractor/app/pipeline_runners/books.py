from app.src.extractor.file_reader import FileReader
from app.src.loader.mongo_loader import MongoLoader
from app.src.pipeline import Pipeline
from app.src.validator.book_validator import BookValidator

strategy={
    'extractor_type':FileReader('book_data.csv', chunksize=10 ** 4),
    'validator_type':BookValidator(),
    'loader_type':MongoLoader(target='books')
}