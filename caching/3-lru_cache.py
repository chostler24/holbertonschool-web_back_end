#!/usr/bin/env python3
"""
Create a class LRUCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Class definition of LRUCache that inherits from BaseCaching"""
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Put method assigns item value for key to dict"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)

        if len(self.queue) > self.MAX_ITEMS:
            oldest_key = self.queue.pop(0)
            del self.cache_data[oldest_key]
            print("DISCARD: {}".format(oldest_key))

    def get(self, key):
        """Get method returns value in dict linked to key"""
        if key is None or key not in self.cache_data:
            return None

        self.queue.remove(key)
        self.queue.append(key)

        return self.cache_data[key]
