from abc import ABC


class DataReader(ABC):
    def __init__(self, actions_source, books_source):
        self.actions_source = actions_source
        self.books_source = books_source

    def read_data(self, uid, book_list):
        raise NotImplementedError
