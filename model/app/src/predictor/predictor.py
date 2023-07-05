from abc import ABC


class Predictor(ABC):
    def predict(self, df_total, valid_books, book_list):
        raise NotImplementedError
