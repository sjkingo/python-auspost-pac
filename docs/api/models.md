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



<br><hr>



## *class* `auspost_pac.models.Parcel`

### Arguments: `Parcel(height=0, weight=0, length=0, width=0)`

A simple class to represent a parcel with 3 dimmensions and a weight.

You must call it with all 4 keyword arguments.

### `height`

The parcel's height.

### `weight`

The parcel's weight.

### `length`

The parcel's length.

### `width`

The parcel's width.



<br><hr>



## *class* `auspost_pac.models.PostageService`

Each postage service option return is wrapped in this class. It should not be
called directly.


### Attributes

### `code`

The key of this service option. Will be unique to all options.

### `max_extra_cover`

The maximum amount of extra postal insurance that may be purchased (as a
`decimal.Decimal` instance).

### `name`

The name of this postage service.

### `options`

A list of available service options (`ServiceOption` instances).

### `price`

The cost of this postage option as a `decimal.Decimal` instance.



<br><hr>



## class `auspost_pac.models.ServiceOption`

A service option as returned by the PAC. This should not be called directly.

### Attributes

### `code`

The unique name for this service option.

### `name`

The name of this service option.

### `suboptions`

A list of available suboptions (`ServiceSubOption` instances).



<br><hr>


## class `auspost_pac.models.ServiceSubOption`

This class subclasses `ServiceOption` and has the same attributes. It is used
by the `ServiceOption.suboptions` attribute to differentiate between postal
service options and suboptions.

It should not be called directly.

