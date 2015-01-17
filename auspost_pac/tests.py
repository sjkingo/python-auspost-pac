from unittest import TestCase

from .models import Locality
from .pac import PAC

API_KEY = 'c8cf3045-91d0-40c5-babd-1516a6f78d6d'

class BaseTestCase(TestCase):
    def setUp(self):
        self.api = PAC(API_KEY)

class TestPACCommon(BaseTestCase):
    def test_empty_query(self):
        """
        Tests that the correct exception is raised when an empty query is
        given.
        """
        with self.assertRaises(ValueError) as cm:
            r = self.api.locality_search('')
        self.assertEqual(str(cm.exception), 'query argument must not be empty')

    def test_invalid_query_type(self):
        """
        Tests that when given an invalid type for the query, an exception
        is raised.
        """
        with self.assertRaises(ValueError) as cm:
            r = self.api.locality_search([])
        self.assertEqual(str(cm.exception), 'query argument must be a str or int')

class TestPostcodeLookup(BaseTestCase):
    def test_valid_postcode_list(self):
        """
        Validates that the return from the API is a list of Locality instances.
        """
        r = self.api.locality_search('4500')
        self.assertIsInstance(r, list)
        for l in r:
            self.assertIsInstance(l, Locality)

    def test_empty_result(self):
        """
        Validates that the return from the API (when given a query that does
        not match any valid locality) returns an empty list.
        """
        r = self.api.locality_search('9988')
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 0)

    def test_valid_postcode_state_list(self):
        """
        Validates that the state= kwarg to locality_search works as expected.
        """
        r = self.api.locality_search('4521', state='QLD')
        self.assertEqual(len(r), 8)
        r = self.api.locality_search('4521', state='NSW')
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 0)

    def test_valid_postcode_state_pbx_list(self):
        """
        Validates that the exclude_postbox= kwargs works as expected.
        """
        r = self.api.locality_search('4521', exclude_postbox=False)
        self.assertEqual(len(r), 8)

    def test_valid_postcode_single(self):
        """
        Validates that when only 1 result is returned the API still yields
        a list.
        """
        r = self.api.locality_search('6160')
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 1)
        self.assertIsInstance(r[0], Locality)

    def test_invalid_postcode(self):
        """
        Validates that no error is returned when searching for an invalid
        postcode.
        """
        r = self.api.locality_search('124124124124')
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 0)

    def test_postcode_as_int(self):
        """
        Validates that a query can be given as an int instead of string.
        """
        r = self.api.locality_search(4521)
        self.assertEqual(len(r), 8)

class TestLocalityLookup(BaseTestCase):
    def test_valid_suburb_list(self):
        """
        Validates that the return from the API is a list of Locality instances.
        """
        r = self.api.locality_search('Brisbane')
        self.assertIsInstance(r, list)
        for l in r:
            self.assertIsInstance(l, Locality)

    def test_empty_result(self):
        """
        Validates that the return from the API (when given a query that does
        not match any valid locality) returns an empty list.
        """
        r = self.api.locality_search('Porky Pig and Daffy Duck')
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 0)

    def test_valid_suburb_state_list(self):
        """
        Validates that the state= kwarg to locality_search works as expected.
        """
        r = self.api.locality_search('Ocean', state='QLD')
        self.assertEqual(len(r), 1)
        r = self.api.locality_search('Ocean', state='NSW')
        self.assertEqual(len(r), 1)

    def test_valid_suburb_single(self):
        """
        Validates that when only 1 result is returned the API still yields
        a list.
        """
        r = self.api.locality_search('Ocean View')
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 1)
        self.assertIsInstance(r[0], Locality)

