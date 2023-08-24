#!/usr/bin/env python3
''' Create a clas,s LIFOCache that inherits
from BaseCaching and is a caching system:
'''


BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    ''' A Fifo  Cacheing Class  '''

    def put(self, key, item):
        """ Add an item in the cache
        """
        caches = self.cache_data
        if key is not None and item is not None:
            caches[key] = item
        if len(caches) > BaseCaching.MAX_ITEMS:
            deleted_key = list(caches.keys())[BaseCaching.MAX_ITEMS - 1]
            print(f"DISCARD: {deleted_key}")
            del caches[deleted_key]

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
