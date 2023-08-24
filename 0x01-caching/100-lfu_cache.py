#!/usr/bin/env python3
''' Create a class LFUCache that inherits
from BaseCaching and is a caching system:
'''


BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    ''' A Fifo  Cacheing Class  '''

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.usage_history = {}

    def put(self, key, item):
        """ Add an item in the cache """
        caches = self.cache_data
        if key is not None and item is not None:
            caches[key] = item

        if len(caches) > BaseCaching.MAX_ITEMS:
            max = BaseCaching.MAX_ITEMS
            lfu = list(sorted(self.usage_history.keys()))[0]
            print(f"DISCARD: {lfu}")
            del caches[lfu]
            self.usage_history.pop(lfu)

        self.usage_history[key] = 1

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None

        if key in self.usage_history:
            self.usage_history[key] += 1
        return self.cache_data[key]
