#!/usr/bin/env python3
'''
Creates a class BasicCache that
inherits from BaseCaching and is a caching system:
and is a caching system:
'''

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    ''' A Basic Cacheing Class  '''

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
