import pymongo

from config import mongo
from data_reader.data_reader import DataReader
import pandas as pd


class MongoReader(DataReader):

    def __init__(self, actions_source='actions', books_source='books'):
        super().__init__(actions_source, books_source)
        cli = pymongo.MongoClient(mongo["host"])
        db_name = mongo["db_name"]
        self.db = cli[db_name]
        self.actioon_colletion = self.db[actions_source]
        self.book_colletion = self.db[books_source]
        self.books_selected_fields={'_id': 0, 'book_id': 1, 'price': 1, 'number_of_page': 1,
                                               'publishDate': 1, 'rating': 1, 'categories': 1, 'lang': 1, }

    def read_data_from_mongo(self, uid, book_list):
        actions = list(self.actioon_colletion.find({"AccountId": uid},{'_id': 0}))
        books = list(self.book_colletion.find({"book_id": {"$in": book_list}},self.books_selected_fields))
        dfa = pd.DataFrame.from_dict(actions)
        dfb = pd.DataFrame.from_dict(books)
        # user_books_id=list(map(lambda d: d['book_id'],actions))
        user_books = list(self.book_colletion.find({"book_id": {"$in": list(dfa['book_id'])}},self.books_selected_fields))
        dfu = pd.DataFrame.from_dict(user_books)
        dfb = dfb.append(dfu).drop_duplicates()
        return dfa.to_dict('records'), dfb.to_dict('records')
