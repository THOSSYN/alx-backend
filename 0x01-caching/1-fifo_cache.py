#!/usr/bin/env python3
"""A script that creates a caching system"""

BaseCaching = __import__('0-basic_cache').BaseCaching


class FIFOCache(BaseCaching):
    """A FIFO caching system policy"""
    def __init__(self):
        """Instantiate attributes of the class"""
        super().__init__()

    def put(self, key, item):
        """Assigns value to key in self.cache_data dict"""
        if key is not None or item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key, _  = list(self.cache_data.items())[0]
            del self.cache_data[discard_key]
            print(f"DISCARD: {discard_key}")

    def get(self, key):
        """Gets value equivalent to a key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
