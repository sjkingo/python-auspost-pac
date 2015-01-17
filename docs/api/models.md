# `auspost_pac.models`

## *class* `auspost_pac.models.Locality`

Each locality response returned from the PAC is a `Locality` object. It
provides a simple wrapper around the response and should not be called
directly.

### Attributes

### `as_dict`

Return all the attributes as a dictionary. This may be useful for caching
purposes. The dictionary is mutable, unlike this object's attributes.

### `category`

The category of this locality, e.g. `Delivery Area`.

### `id`

The unique locality ID as given by Australia Post.

### `latitude` and `longitude`

The coordinates of the centre of locality.

### `location`

The locality name, e.g. `OCEAN VIEW`. It will always be returned in captials.

### `postcode`

The 4-digit postal code for this locality, as an `int`.

### `state`

The 2 or 3-digit state code for this locality. Will be one of:

```
['QLD', 'NSW', 'VIC', 'TAS', 'ACT', 'SA', 'WA', 'NT']
```

