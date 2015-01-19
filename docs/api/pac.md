# `auspost_pac.pac`

This document describes the API interface to the PAC.

## *class* `auspost_pac.pac.PAC`(*api_key*, ***kwargs*)

This class provides the main interface to PAC. You must provide it
a valid `api_key` (see [Installation](../installation.md#api-key) for instructions).

It is also possible to override the default API URL. You would almost certainly
not need to do this, but if you do, pass `api_url` to the constructer.

Once you have a `PAC` instance, you can call into the API:

### `locality_search`(*query*, *state=None*, *exclude_postbox=True*)

Run a search against the PAC with the given `query`. This may either be a
complete postcode, or a full or partial location name.

Results will be returned as a list of `Locality` objects.

The following optional arguments are supported:

* `state`: Restrict the search to the state given by its 2 or 3-digit state code (e.g. `QLD`). Defaults to `None`, meaning no restriction.
* `exclude_postbox`: Excludes localities that are Post Boxes only. Defaults to `True`.

### `domestic_parcel_services`(*from_postcode*, *to_postcode*, *parcel*)

Returns a list of all services for a domestic parcel with the given details.

#### Arguments:

* `from_postcode`: the sender's postcode
* `to_postcode`: the receiver's postcode
* `parcel`: a `Parcel` instance representing the dimmensions and weight of the parcel to be sent.

Results will be returned as a list of `PostageService` objects.

