import json
import unittest

from api import app, db

from app import load_user
from constants_book_service import BOOK_REQUEST, BOOK_MODIFY1, BOOK_MODIFY2, BOOK_DELETE1, BOOK_DELETE2


class TestBookService(unittest.TestCase):
    def setUp(self):
        app.config['LOGIN_DISABLED'] = True
        db.create_all(app=app)
        self.app = app.test_client()

    def test_book_create(self):
        request = BOOK_REQUEST
        response = self.app.post('/books', data=json.dumps({'query': request}), content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual("K L", data["data"]['createBook']['book']['author'])

    def test_book_modify(self):
        request = BOOK_REQUEST
        response = self.app.post('/books', data=json.dumps({'query': request}), content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual("K L", data["data"]['createBook']['book']['author'])
        request_modify = BOOK_MODIFY1 + data["data"]['createBook']['book']['id'] + BOOK_MODIFY2
        response_modify = self.app.post('/books', data=json.dumps({'query': request_modify}),
                                        content_type='application/json')
        data_modify = json.loads(response_modify.get_data())
        print(data_modify)
        self.assertEqual(True, data_modify["data"]['updateBook']['success'])

    def test_book_delete(self):
        request = BOOK_REQUEST
        response = self.app.post('/books', data=json.dumps({'query': request}), content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual("K L", data["data"]['createBook']['book']['author'])
        request_modify = BOOK_DELETE1 + data["data"]['createBook']['book']['id'] + BOOK_DELETE2
        response_modify = self.app.post('/books', data=json.dumps({'query': request_modify}),
                                        content_type='application/json')
        data_modify = json.loads(response_modify.get_data())
        self.assertEqual(True, data_modify["data"]['deleteBook']['success'])
