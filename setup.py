from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hmsclient-hive-3',
    version='0.1.1',

    description='A package interact with the Hive metastore (API version 3.0) via the Thrift protocol',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/itamarla/hmsclient-hive-3',

    # Author details
    author='https://github.com/itamarla/hmsclient-hive-3',
    author_email='itamar@itamar.org',

    # Choose your license
    license='Apache 2.0',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Information Technology',
        'Topic :: Database',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='hive data database thrift metastore',
    packages=find_packages(exclude=['tests', 'docs']),

    install_requires=['thrift', 'click'],

    extras_require={
        'dev': ['pytest'],
        'test': ['pytest'],
    },
    )
