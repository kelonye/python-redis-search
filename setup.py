#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='reds',
    version='0.0.1',
    description='Simple full text search library for python backed by Redis.',
    author='Mitchel Kelonye',
    author_email='kelonyemitchel@gmail.com',
    url='https://github.com/kelonye/python_redis_search',
    packages=find_packages(exclude=['test.py']),
    install_requires = ['redis'],
    license='MIT License',
    zip_safe=True)
