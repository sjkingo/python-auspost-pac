from setuptools import find_packages, setup

from auspost_pac import __version__ as version

setup(
    name='python-auspost-pac',
    version=version,
    license='BSD',
    author='Sam Kingston',
    author_email='sam@sjkwi.com.au',
    description='Python API for Australia Post\'s Postage Assessment Calculator (pac).',
    url='https://github.com/sjkingo/python-auspost-pac',
    install_requires=[
        'cached_property',
        'frozendict',
        'requests',
    ],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python',
    ],
)
