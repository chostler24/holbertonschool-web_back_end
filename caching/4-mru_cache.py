#!/usr/bin/env python3
"""
Create a class MRUCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Class definition MRUCache that inherits from BaseCaching"""
    def __init__(self):
        """initialize"""
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

        if len(self.cache_data) >= self.MAX_ITEMS:
            recent_key = self.queue.pop()
            del self.cache_data[recent_key]
            print("DISCARD: {}".format(recent_key))

    def get(self, key):
        """Get method returns value in dict linked to key"""
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
