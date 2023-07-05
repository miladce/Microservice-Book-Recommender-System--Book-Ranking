from abc import ABC


class DataValidator(ABC):
    def validate_data(self, data):
        raise NotImplementedError
