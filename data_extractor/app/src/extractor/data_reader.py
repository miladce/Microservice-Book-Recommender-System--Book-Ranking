from abc import ABC


class DataReader(ABC):
    def __init__(self, source, chunksize):
        self.source = source
        self.chunksize = chunksize

    def read_data(self, checkpoint):
        raise NotImplementedError
