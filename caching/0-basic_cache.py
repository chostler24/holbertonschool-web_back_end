#!/usr/bin/env python3
"""
Create a class BasicCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class definition of Basic Cache that inherits from BaseCaching"""
    def put(self, key, item):
        """Put method that assigns item value to key in dict"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get method that returns value in dict to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
