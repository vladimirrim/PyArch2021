import json
from urllib.request import urlopen

API = 'https://www.googleapis.com/books/v1/volumes'
ISBN_QUERY = '?q=isbn:'
TITLE_QUERY = '?q=title:'


class GoogleBooksAPIManager:

    def get_book_info_by_isbn(self, isbn):
        return self.__dispatch_query(API + ISBN_QUERY + isbn)

    def get_book_info_by_title(self, title):
        return self.__dispatch_query(API + ISBN_QUERY + title)

    def __dispatch_query(self, query):
        resp = urlopen(query)
        book_data = json.load(resp)
        if len(book_data["items"]) > 0:
            return book_data["items"][0]["volumeInfo"]
        else:
            return None
