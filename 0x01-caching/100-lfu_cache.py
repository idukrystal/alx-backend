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
            lfu = sorted(self.usage_history.items(),
                         key=lambda item: item[1]
                         )[0][0]
            print(f"DISCARD: {lfu}")
            del caches[lfu]
            self.usage_history.pop(lfu)
            # print(f">>> DEBUG full({key}): {self.usage_history}")
        if key not in self.usage_history:
            self.usage_history[key] = 1
        else:
            self.usage_history[key] += 1
        # print(f">>> DEBUG put({key}): {self.usage_history}")

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None

        if key in self.usage_history:
            self.usage_history[key] += 1
            # print(f">>> DEBUG get({key}): {self.usage_history}")
        return self.cache_data[key]
