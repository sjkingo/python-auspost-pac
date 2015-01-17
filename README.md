# python-auspost-pac

Python API for Australia Post's [Postage Assessment
Calculator](https://developers.auspost.com.au/apis/pac/getting-started) (pac).
This includes support for looking up and validating postcodes and localities.

It requires an API key to be created at the [Australia Post website](https://developers.auspost.com.au/apis/pacpcs-registration).

## Installation

Simply install from PyPi:

```
$ pip install python-auspost-pac
```

It is recommended this be done in a virtualenv.

## Running tests

A full test suite is provided and can be run by checking out the source and
running `nosetests`:

```
$ git clone https://github.com/sjkingo/python-auspost-pac.git
$ nosetests --with-coverage --cover-package=auspost_pac
```

## API documentation

