import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from config import model_path

class Preprocessor:
    def preprocess(self, dfa, dfb, uid):
        dfb['publishYear'] = dfb['publishDate'].str.split('/', expand=True)[0]

        with open(f'{model_path}year_freq.pkl', "rb") as f:
            year_freq = pickle.load(f)
        missing = dfb['publishYear'].isnull()
        dfb.loc[missing, 'publishYear'] = np.random.choice(year_freq.index, size=len(dfb[missing]), p=year_freq.values)
        dfb['publishYear'] = dfb['publishYear'].astype(int)

        with open(f'{model_path}price_page_scaler.pkl', "rb") as f:
            scaler = pickle.load(f)
        dfb[['price', 'number_of_page']] = scaler.transform(dfb[['price', 'number_of_page']])

        def one_mode(modearr):
            if len(modearr) > 0:
                return modearr[0]
            if len(modearr) == 0:
                return None

        joined = dfa.merge(dfb[['book_id', 'number_of_page', 'price', 'categories']], on='book_id', how='left')
        reduced = joined.groupby('AccountId').agg({'price': ['mean', 'std'],
                                                   'number_of_page': ['mean', 'std'],
                                                   'categories': lambda x: one_mode(pd.Series.mode(x))})
        dfu = reduced.dropna(subset=[('number_of_page', 'mean')])
        dfu.fillna(0, inplace=True)

        if len(dfu) == 0:
            return -1

        book_selected_features = ['book_id', 'price', 'number_of_page', 'categories', 'lang', 'publishYear']
        valid_books = set(dfb['book_id'])

        df_total = dfb[book_selected_features]
        df_total['AccountId'] = uid
        df_total = pd.merge(dfu, df_total, on=['AccountId'])

        df_total = pd.get_dummies(df_total, prefix={('categories', '<lambda>'): 'userC',
                                                    'categories': 'bookC',
                                                    'lang': 'lang'},
                                  drop_first=False)
        with open(f'{model_path}total_columns.pkl', "rb")as f:
            total_columns = pickle.load(f)
        return df_total.reindex(columns=total_columns, fill_value=0), valid_books
