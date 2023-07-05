from app.src.predictor.predictor import Predictor
import pickle
from pandas import DataFrame

from config import model_path


class Lgbm(Predictor):

    def predict(self, df_total: DataFrame, valid_books, book_list):
        with open(f'{model_path}pickle_dump_lgbm.pkl', "rb")as f:
            model = pickle.load(f)
        train_cols = list(df_total.drop(columns=['AccountId', 'book_id', 'y']).columns)

        candid_books = []
        for book in book_list:
            if book in valid_books:
                candid_books.append(book)
        if len(candid_books) > 0:
            df_total = df_total[df_total['book_id'].isin(book_list)]
            df_total['score'] = (model.predict(df_total[train_cols]))
            df_total['rank'] = df_total['score'].rank(method='min', ascending=False)
            return df_total[['score', 'rank', 'book_id']].to_dict('record')
