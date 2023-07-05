import pandas as pd
from config import data_path
from data_reader.data_reader import DataReader


class FileReader(DataReader):
    def __init__(self, actions_source='actions.csv', books_source='book_data.csv'):
        super().__init__(f'{data_path}{actions_source}', f'{data_path}{books_source}')

    def read_data(self, uid, book_list):
        dfa = pd.read_csv(self.actions_source).rename(columns={"BookId": "book_id"})
        dfa = dfa[dfa['AccountId'] == uid]

        books = pd.read_csv(self.books_source)
        dfb = books[books['book_id'].isin(book_list)]
        dfb = dfb.append(books[books['book_id'].isin(dfa['book_id'])]).drop_duplicates()
        return dfa, dfb