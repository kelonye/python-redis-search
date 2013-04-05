#!/usr/bin/env python

import re
import string
import redis

class Search:

    mapper = {}

    def __init__(self, namespace, redis_client=None):
        self.namespace = namespace
        if not redis_client:
            redis_client = redis.StrictRedis()
        self.redis_client = redis_client

    def __resolve__(self, txt):
        txt = txt.lower()
        txt = self.__remove_non_ascii__(txt)
        txt = self.__remove_vowels__(txt)
        txt = self.__remove_dups__(txt)
        txt = self.__process_metaphone__(txt)
        return txt

    # method to remove vowels from a txt
    def __remove_vowels__(self, txt):
        for vowel in ['a', 'e', 'i', 'o', 'u']:
            txt = txt.replace(vowel, '')
        return txt

    # method to remove signs from a txt
    def __remove_non_ascii__(self, txt):
        for char in txt:
            if char not in string.ascii_lowercase:
                txt = txt.replace(char, '')
        return txt

    # method to remove duplicate char from a txt
    def __remove_dups__(self, txt):
        return txt

    # method to find metaphone codes
    def __process_metaphone__(self, txt):
        for key, value in self.mapper.iteritems():
            for char in value:
                txt = txt.replace(char, key)
        return txt

    # method to index a txt
    def push(self, index, txt):
        self.redis_client.hset(self.namespace, index, txt)

    # method to match query_txt with indexed txts
    def query(self, query_txt):
        
        items = self.redis_client.hgetall(self.namespace)

        results = []
        for key, value in items.iteritems():
            if self.__resolve__(value) == self.__resolve__(query_txt):
                results.append(key)
        return results

SWAHILI = {
    'b': ['p'],
    'ch': ['j', 'sh'],
    'd': ['t'],
    'dh': ['th'],
    'f': ['v'],
    'g': ['k'],
    #'j': ['ch'],
    #'k': ['g'],
    'l': ['r'],
    #'p': ['b'],
    #'r': ['l'],
    's': ['z'],
    #'sh': ['ch'],
    #'t': ['d'],
    #'v': ['f'],
    #'z': ['s']
}

class SwahiliSearch(Search):
    mapper = SWAHILI
