# Installation

Installing `python-auspost-pac` is as simple as:

```
$ pip install python-auspost-pac
```

This will install the latest stable release.

Alternatively you may install the latest development version directly from
GitHub:

```
$ pip install -e git+https://github.com/sjkingo/python-auspost-pac.git
```

## Verify installed version

To verify the installation, check the module's `__version__` string:

```python
>>> from auspost_pac import __version__
>>> __version__
'0.9.0'
```

## API key

The module requires you to register an API key at Australia Post's website
and pass it when using the API.

Go to the [PAC and Postcode Search
Registration](https://developers.auspost.com.au/apis/pacpcs-registration) page
to get your API key.
