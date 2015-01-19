from cached_property import cached_property
from decimal import Decimal
from frozendict import frozendict

class Locality(object):
    """
    Represents a locality (place) returned by the API.
    """

    def __init__(self, locality_dict):
        self._d = frozendict(locality_dict)

    def __str__(self):
        return self.location

    def __repr__(self):
        return '<Locality \'{}\'>'.format(self.location)

    @property
    def as_dict(self):
        """
        Return all the attributes as a dictionary. This may be useful for
        caching purposes. The dictionary is mutable, unlike this object's
        attributes.
        """
        return dict(self._d)

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

class Parcel(object):
    """
    Represents a parcel with 3 dimmensions and a weight.
    """

    height = 0
    weight = 0
    length = 0
    width = 0

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if not hasattr(self, k):
                raise ValueError('Parcel object does not have a {} attribute'.format(k))
            setattr(self, k, v)

class PostageService(object):
    """
    Represents a postage service as returned by the PAC.
    """

    def __init__(self, service_dict):
        self._d = frozendict(service_dict)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<PostageService \'{}\'>'.format(self.code)

    @property
    def code(self):
        return self._d.get('code')

    @property
    def max_extra_cover(self):
        return Decimal(str(self._d.get('max_extra_cover')))

    @property
    def name(self):
        return self._d.get('name')

    # Cache this so we're not constructing a new list of options all the time
    @cached_property
    def options(self):
        return [ServiceOption(o) for o in self._d.get('options').get('option')]

    @property
    def price(self):
        return Decimal(self._d.get('price'))

class ServiceOption(object):
    """
    Represents a postal service option. May contain suboptions which are
    represented by ServiceSubOption instances.
    """

    def __init__(self, option_dict):
        self._d = frozendict(option_dict)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<ServiceOption \'{}\'>'.format(self.code)

    @property
    def code(self):
        return self._d.get('code')

    @property
    def name(self):
        return self._d.get('name')

    # Cache this so we're not constructing a new list of options all the time
    @cached_property
    def suboptions(self):
        options = self._d.get('suboptions', {}).get('option')
        if options is None:
            return []
        if type(options) != list:
            options = [options]
        return [ServiceSubOption(o) for o in options]

class ServiceSubOption(ServiceOption):
    """
    Represents any suboptions for a postal service. Typically these are extra
    services such as extra cover or signature on delivery.
    This class is identical to ServiceOption and only exists to differentiate
    between the two.
    """

    def __repr__(self):
        return '<ServiceSubOption \'{}\'>'.format(self.code)
