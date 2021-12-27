import json
import unittest

from api import app, db
from app import load_user
from constants_review_service import REVIEW_REQUEST, REVIEW_MODIFY1, REVIEW_MODIFY2, REVIEW_DELETE1, REVIEW_DELETE2


class TestReviewService(unittest.TestCase):
    def setUp(self):
        app.config['LOGIN_DISABLED'] = True
        db.create_all(app=app)
        self.app = app.test_client()

    def test_review_create(self):
        request = REVIEW_REQUEST
        response = self.app.post('/reviews', data=json.dumps({'query': request}), content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(2, data["data"]['createReview']['review']['rating'])

    def test_review_modify(self):
        request = REVIEW_REQUEST
        response = self.app.post('/reviews', data=json.dumps({'query': request}), content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(2, data["data"]['createReview']['review']['rating'])
        request_modify = REVIEW_MODIFY1 + data["data"]['createReview']['review']['id'] + REVIEW_MODIFY2
        response_modify = self.app.post('/reviews', data=json.dumps({'query': request_modify}),
                                        content_type='application/json')
        data_modify = json.loads(response_modify.get_data())
        self.assertEqual(True, data_modify["data"]['updateReview']['success'])

    def test_review_delete(self):
        request = REVIEW_REQUEST
        response = self.app.post('/reviews', data=json.dumps({'query': request}), content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(2, data["data"]['createReview']['review']['rating'])
        request_modify = REVIEW_DELETE1 + data["data"]['createReview']['review']['id'] + REVIEW_DELETE2
        response_modify = self.app.post('/reviews', data=json.dumps({'query': request_modify}),
                                        content_type='application/json')
        data_modify = json.loads(response_modify.get_data())
        self.assertEqual(True, data_modify["data"]['deleteReview']['success'])
