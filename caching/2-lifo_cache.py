#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Class definition LIFOCache inherited from BaseCaching"""
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Put method assigns item value for key to dict"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) >= self.MAX_ITEMS:
                lastkey = self.stack.pop()
                del self.cache_data[lastkey]
                print("DISCARD: {}".format(lastkey))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get method returns value in dict linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
