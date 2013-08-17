#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='reds',
    version='0.0.1',
    description='Simple full text search library for python backed by Redis.',
    author='Mitchel Kelonye',
    author_email='kelonyemitchel@gmail.com',
    url='https://github.com/kelonye/python-redis-search',
    packages=['reds',],
    package_dir = {'reds': 'lib'},
    install_requires = ['redis'],
    license='MIT License',
    zip_safe=True)
