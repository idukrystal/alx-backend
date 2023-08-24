#!/usr/bin/env python3
''' Create a class LRUCache that inherits
from BaseCaching and is a caching system:
'''


BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    ''' A Fifo  Cacheing Class  '''

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.usage_history = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        caches = self.cache_data
        if key is not None and item is not None:
            caches[key] = item
            if key in self.usage_history:
                self.usage_history.remove(key)
            self.usage_history.insert(0, key)

        if len(caches) > BaseCaching.MAX_ITEMS:
            max = BaseCaching.MAX_ITEMS
            lru = self.usage_history[- 1]
            print(f"DISCARD: {lru}")
            del caches[lru]
            self.usage_history.remove(lru)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None

        if key in self.usage_history:
            self.usage_history.remove(key)
            self.usage_history.insert(0, key)
        return self.cache_data[key]
