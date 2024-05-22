#!/usr/bin/env python3
"""Task 1"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
