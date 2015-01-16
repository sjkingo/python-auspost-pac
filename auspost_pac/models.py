
class Locality(object):
    """
    Represents a locality (place) returned by the API.
    """

    def __init__(self, locality_dict):
        self._d = locality_dict

    def __str__(self):
        return self.location

    def __repr__(self):
        return '<Locality \'{}\'>'.format(self.location)

    @property
    def category(self):
        return self._d.get('category')

    @property
    def id(self):
        return self._d.get('id')

    @property
    def latitude(self):
        return self._d.get('latitude')

    @property
    def longitude(self):
        return self._d.get('longitude')

    @property
    def location(self):
        return self._d.get('location')

    @property
    def postcode(self):
        return self._d.get('postcode')

    @property
    def state(self):
        return self._d.get('state')
