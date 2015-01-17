# Running the tests

A full test suite is provided using Python's `unittest` and `nose`. You must check out
the full source to run the tests:

```
$ git clone https://github.com/sjkingo/python-auspost-pac.git
$ cd python-auspost-pac
```

Some extra dependencies are required:

```
$ pip install nose coveralls
```

Now you can run the tests:

```
$ ./test.sh
```

Which simply calls:

```
$ nosetests --with-coverage --cover-package=auspost_pac
```
