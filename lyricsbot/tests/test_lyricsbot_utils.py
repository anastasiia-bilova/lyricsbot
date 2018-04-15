"""
Tests for custom implementation of built-in Python methods called `lib`.
"""
import unittest

from lyricsbot.lyricsbot_utils import parse_url_db


class TestLib(unittest.TestCase):
    """
    Tests for custom implementation built-in Python methods.
    """

    def test_parse_url_database(self):
        """
        Test.
        """
        database_url = \
            'postgres://eerfdsfassdf:fgfdgdfg@baasu.db.elephantsql.com:5432/eerfdsfassdf'
        expected_result = {
            'user': 'eerfdsfassdf',
            'database': 'eerfdsfassdf',
            'password': 'fgfdgdfg',
            'port': '5432',
            'host': 'baasu.db.elephantsql.com'
        }
        response = parse_url_db(database_url)

        self.assertEqual(expected_result, response)
