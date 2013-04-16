#!/usr/bin/env python
import unittest
from urllib2 import urlopen

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import reds
import redis

class SearchT(unittest.TestCase):

    def setUp(self):
        self.redis_client = redis.StrictRedis(db=12)
        self.reds_client = reds.SwahiliSearch('villages', self.redis_client)

    def tearDown(self):
        self.redis_client.flushdb()

    def test_search(self):
        villages = ['Gatwekera', 'Patwekera']
        for index, name in enumerate(villages):
            self.reds_client.push(index, name)

        results = self.reds_client.query('Gatwekera')
        assert len(results) == 1
        assert int(results[0]) == 0

    def test_case(self):
        villages = ['Gatwekera', 'Patwekera']
        for index, name in enumerate(villages):
            self.reds_client.push(index, name)

        results = self.reds_client.query('gatwEkerA')
        assert len(results) == 1
        assert int(results[0]) == 0

    def test_omission(self):
        villages = ['Gatwekera', 'Patwekera']
        for index, name in enumerate(villages):
            self.reds_client.push(index, name)

        results = self.reds_client.query('Gatweker')
        assert len(results) == 1
        assert int(results[0]) == 0

    def test_metaphone(self):
        villages = ['Gatwekera', 'Patwekera']
        for index, name in enumerate(villages):
            self.reds_client.push(index, name)

        results = self.reds_client.query('Catwekera')
        assert len(results) == 0

        results = self.reds_client.query('Katwekera')
        assert len(results) == 1
        assert int(results[0]) == 0

        results = self.reds_client.query('Batwekera')
        assert len(results) == 1
        assert int(results[0]) == 1

    def test_vowel(self):
        villages = ['Gatwekera', 'Patwekera']
        for index, name in enumerate(villages):
            self.reds_client.push(index, name)

        results = self.reds_client.query('Getwekera')
        assert len(results) == 1
        assert int(results[0]) == 0

        results = self.reds_client.query('Peaetwekera')
        assert len(results) == 1
        assert int(results[0]) == 1

    def test_dup(self):
        villages = ['Gatwekera', 'Patwekera']
        for index, name in enumerate(villages):
            self.reds_client.push(index, name)

        results = self.reds_client.query('Gattttttwekera')
        assert len(results) == 1
        assert int(results[0]) == 0

        results = self.reds_client.query('Pppatwekkerrra')
        assert len(results) == 1
        assert int(results[0]) == 1

if __name__ == '__main__':
    unittest.main()