#!/usr/bin/env python3
"""Module for task 2"""

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''Basic cache module for storing and retrieving
    from a dictionary and removes first item if max length is reached
    '''

    def __init__(self):
        '''initializer of cache instance'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Adds item to cache'''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key_item, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key_item)

    def get(self, key):
        '''Retrieves item from cache'''
        return self.cache_data.get(key, None)
