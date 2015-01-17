# python-auspost-pac

Python API for Australia Post's [Postage Assessment
Calculator](https://developers.auspost.com.au/apis/pac/getting-started) (pac).
This includes support for looking up and validating postcodes and localities.

It requires an API key to be created at the [Australia Post website](https://developers.auspost.com.au/apis/pacpcs-registration).

[![Latest Version](https://pypip.in/version/python-auspost-pac/badge.svg?style=flat)](https://pypi.python.org/pypi/python-auspost-pac/)
[![Supported Python versions](https://pypip.in/py_versions/python-auspost-pac/badge.svg?style=flat)](https://pypi.python.org/pypi/python-auspost-pac/)
[![License](https://pypip.in/license/python-auspost-pac/badge.svg?style=flat)](https://github.com/sjkingo/python-auspost-pac/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/sjkingo/python-auspost-pac.svg?branch=master)](https://travis-ci.org/sjkingo/python-auspost-pac)
[![Coverage Status](https://coveralls.io/repos/sjkingo/python-auspost-pac/badge.svg)](https://coveralls.io/r/sjkingo/python-auspost-pac)

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

