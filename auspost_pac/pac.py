import requests

from .models import Locality

class PAC(object):
    """
    Postage Assessment Calculator.
    """

    _api_url = 'https://auspost.com.au/api'
    _api_format = 'json'

    def __init__(self, api_key, api_url='https://auspost.com.au/api'):
        self._api_url = api_url
        self._api_key = api_key

    def _make_request(self, url, **kwargs):
        params = {k: v for (k, v) in kwargs.items() if v is not None}
        full_url = '{}/{}.{}'.format(self._api_url, url, self._api_format)
        headers = {'auth-key': self._api_key}

        r = requests.get(full_url, params=params, headers=headers)
        r.raise_for_status()
        return r.json()

    def locality_search(self, query, state=None, exclude_postbox=True):
        """
        Searches for the given locality (place) or postcode and returns a list
        of Locality objects that match it.

        If no results are found, returns an empty list.

        You may specify state=True to filter by a 3-letter state code, or
        exclude_postbox=False to include post office boxes (excluded by
        default).
        """

        url = 'postcode/search'
        pbf = True if exclude_postbox else None

        r = self._make_request(url, q=query, state=state, excludepostboxflag=pbf)
        if 'localities' not in r or r['localities'] == '':
            return []

        locality_list = r['localities']['locality']
        if type(locality_list) == dict:
            locality_list = [locality_list]

        return [Locality(l) for l in locality_list]
