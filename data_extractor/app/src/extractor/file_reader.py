import pandas as pd

from app.src.extractor.data_reader import DataReader
from config import data_path


class FileReader(DataReader):
    def __init__(self, source, chunksize):
        super().__init__(f'{data_path}{source}', chunksize)
        self.df = pd.read_csv(self.source)

    def read_data(self, checkpoint):
        return self.df[checkpoint:checkpoint + self.chunksize]

    # def batch_generator(self):
    #     chunksize = self.chunksize
    #     with pd.read_csv(self.source, chunksize=chunksize) as reader:
    #         for chunk in reader:
    #             yield chunk
    #
    # def read_data(self):
    #     try:
    #         return self.read_one_batch.__next__()
    #     except:
    #         return None
