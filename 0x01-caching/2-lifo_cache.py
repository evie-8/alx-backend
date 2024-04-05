#!/usr/bin/env python3
"""Module for task 3"""

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''Basic cache module for storing and retrieving
    from a dictionary and removes last item if max length is reached
    '''

    def __init__(self):
        '''initializer of cache instance'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Adds item to cache'''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key_item, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key_item)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        '''Retrieves item from cache'''
        return self.cache_data.get(key, None)
