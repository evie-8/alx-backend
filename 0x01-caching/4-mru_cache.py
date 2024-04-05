#!/usr/bin/env python3
"""Module for task 4"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
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
                mru_key_item, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key_item)

            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item


    def get(self, key):
        '''Retrieves item from cache'''
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
