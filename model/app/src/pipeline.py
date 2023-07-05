import pandas as pd
from app.src.predictor.lgbm import Lgbm
from app.src.preprocessor.preprocessor import Preprocessor


class Pipeline:

    def __init__(self, input: dict, strategy=None):
        if strategy is None:
            self.set_default_strategy()
        self.parse_strategy(strategy)
        self.parse_input(input)

    def parse_strategy(self, strategy: dict = None):
        if strategy:
            if strategy['preprocessor_type']:
                self.preprocessor = strategy['preprocessor_type']
            if strategy['predictor_type']:
                self.predictor = strategy['predictor_type']

    def set_default_strategy(self):
        self.preprocessor = Preprocessor()
        self.predictor = Lgbm()

    def parse_input(self, input):
        self.uid = input['uid']
        self.book_list = input['book_list']
        self.dfa = pd.DataFrame.from_dict(input['dfa'])
        self.dfb = pd.DataFrame.from_dict(input['dfb'])

    def run(self):
        df_total, valid_books = self.preprocessor.preprocess(self.dfa, self.dfb, self.uid)
        return self.predictor.predict(df_total, valid_books, self.book_list)
