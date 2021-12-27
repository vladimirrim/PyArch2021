import unittest

from api.book.mutations import parse_author


class TestParsing(unittest.TestCase):
    def test_parsing_success(self):
        res = parse_author("k l ")
        self.assertEquals("K L", res)

    def test_validate_empty(self):
        res = parse_author("")
        self.assertIsNone(res)

    def test_parsing_too_many_words(self):
        res = parse_author("k l l")
        self.assertIsNone(res)
