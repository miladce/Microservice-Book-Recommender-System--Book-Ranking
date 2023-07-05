from abc import ABC


class DataLoader(ABC):
    def load_data(self, json_data):
        raise NotImplementedError
