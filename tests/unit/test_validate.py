import unittest

from api.review.mutations import validate_rating


class TestValidation(unittest.TestCase):
    def test_validate_success(self):
        res = validate_rating(3)
        self.assertEquals(3, res)

    def test_validate_string(self):
        res = validate_rating("3")
        self.assertEquals(3, res)

    def test_validate_out_of_range(self):
        res = validate_rating(-1)
        self.assertIsNone(res)
