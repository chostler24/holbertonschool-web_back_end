#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class definition FIFOCache that inherits from BaseCaching"""
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Put method that assigns item value to key in dict"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.queue.append(key)

        if len(self.queue) > self.MAX_ITEMS:
            oldkey = self.queue.pop(0)
            del self.cache_data[oldkey]
            print("DISCARD: {}".format(oldkey))

    def get(self, key):
        """Get method that returns value in dict linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
