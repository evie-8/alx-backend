#!/usr/bin/env python2
"""Module for task 0"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Basic cache module for storing and retrieving
    from a dictionary
    '''

    def put(self, key, item):
        '''Adds item to cache'''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''Retrieves item from cache'''
        return self.cache_data.get(key, None)
