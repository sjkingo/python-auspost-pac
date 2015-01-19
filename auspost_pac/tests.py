from decimal import Decimal
import random
from unittest import TestCase

from .models import *
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

class TestLocalityModel(BaseTestCase):
    """
    Tests the models.Locality class.
    """

    def test_locality_model(self):
        """
        Validates the Locality class yields the correct attributes.
        """
        r = self.api.locality_search('Ocean View', state='QLD')
        l = r[0]
        self.assertEqual(str(l), 'OCEAN VIEW')
        self.assertEqual(repr(l), '<Locality \'OCEAN VIEW\'>')
        self.assertEqual(l.category, 'Delivery Area')
        self.assertEqual(l.id, 10210)
        self.assertEqual(l.latitude, -27.143427)
        self.assertEqual(l.longitude, 152.817476)
        self.assertEqual(l.location, 'OCEAN VIEW')
        self.assertEqual(l.postcode, 4521)
        self.assertEqual(l.state, 'QLD')
        self.assertEqual(l.as_dict, dict(l._d))

class TestParcelModel(BaseTestCase):
    """
    Tests the models.Parcel class. This doesn't require API access.
    """

    def setUp(self):
        attribs = ['weight', 'height', 'length', 'width']
        def _randint():
            return random.randint(1, 100)
        self.d = {}
        for k in attribs:
            self.d[k] = _randint()

    def test_empty_attribs(self):
        p = Parcel()
        for k in self.d.keys():
            self.assertEqual(getattr(p, k), 0)

    def test_all_correct_attribs(self):
        p = Parcel(**self.d)
        for k, v in self.d.items():
            self.assertEqual(getattr(p, k), v)

    def test_missing_attribs(self):
        d = dict(self.d)
        del d['weight']
        p = Parcel(**d)
        for k, v in d.items():
            self.assertEqual(getattr(p, k), v)
        self.assertEqual(p.weight, 0)

    def test_extra_attribs(self):
        d = dict(self.d)
        d['extra'] = 'should raise ValueError'
        self.assertRaises(ValueError, Parcel, **d)

class TestDomesticParcelLookup(BaseTestCase):
    def setUp(self):
        self.parcel = Parcel(width=10, length=10, height=10, weight=1)
        super(TestDomesticParcelLookup, self).setUp()
        self.p = self.api.domestic_parcel_services(4000, 2000, self.parcel)

    def test_str(self):
        self.assertEqual(str(self.p[0]), self.p[0].name)

    def test_repr(self):
        self.assertEqual(repr(self.p[0]), '<PostageService \'{}\'>'.format(self.p[0].code))

    def test_valid_regular_parcel(self):
        self.assertIs(type(self.p), list)
        self.assertEqual(len(self.p), 4)

        expected_dict = {
            'AUS_PARCEL_REGULAR': {
                'name': 'Parcel Post',
                'price': Decimal('13.50'),
                'max_extra_cover': 5000,
            },
            'AUS_PARCEL_REGULAR_SATCHEL_3KG': {
                'name': 'Parcel Post Medium (3Kg) Satchel',
                'price': Decimal('13.40'),
                'max_extra_cover': 5000,
            },
            'AUS_PARCEL_EXPRESS': {
                'name': 'Express Post',
                'price': Decimal('19.10'),
                'max_extra_cover': 5000,
            },
            'AUS_PARCEL_EXPRESS_SATCHEL_3KG': {
                'name': 'Express Post Medium (3Kg) Satchel',
                'price': Decimal('14.80'),
                'max_extra_cover': 5000,
            },
        }
        self.assertCountEqual([o.code for o in self.p], expected_dict.keys())

        for option in self.p:
            self.assertIs(type(option), PostageService)
            expected_o = expected_dict[option.code]
            self.assertEqual(option.name, expected_o['name'])
            self.assertEqual(option.price, expected_o['price'])
            self.assertEqual(option.max_extra_cover, expected_o['max_extra_cover'])

    def test_invalid_parcel_argument(self):
        self.assertRaises(ValueError, self.api.domestic_parcel_services, 4000, 2000, {})

    def test_service_options(self):
        reg = self.p[0]
        self.assertIs(type(reg.options), list)
        self.assertEqual(len(reg.options), 2)

        expected_options = {
            'AUS_SERVICE_OPTION_STANDARD': {
                'name': 'Standard Service',
            },
            'AUS_SERVICE_OPTION_SIGNATURE_ON_DELIVERY': {
                'name': 'Signature on Delivery',
            },
        }
        self.assertCountEqual([o.code for o in reg.options], expected_options.keys())

        for o in reg.options:
            self.assertIs(type(o), ServiceOption)
            expected_o = expected_options[o.code]
            self.assertEqual(o.name, expected_o['name'])
            self.assertEqual(str(o), expected_o['name'])

    def test_service_suboptions(self):
        sig = None
        for i in self.p[0].options:
            if i.code == 'AUS_SERVICE_OPTION_SIGNATURE_ON_DELIVERY':
                sig = i.suboptions
                break
        self.assertIs(type(sig), list)

        for o in sig:
            self.assertIs(type(o), ServiceSubOption)
            # we don't need to test attributes since ServiceSubOption inherits from
            # ServiceOption, tested above

    def test_empty_suboptions(self):
        d = dict(self.p[0].options[0]._d)
        del d['suboptions']
        o = ServiceOption(d)
        self.assertEqual(o.suboptions, [])
