#!/usr/bin/env python3
"""A script that creates a caching system"""

BaseCaching = __import__('0-basic_cache').BaseCaching


class LIFOCache(BaseCaching):
    """A FIFO caching system policy"""
    def __init__(self):
        """Instantiate attributes of the class"""
        super().__init__()

    def put(self, key, item):
        """Assigns value to key in self.cache_data dict"""
        discard_key = None

        if key is not None or item is not None:
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key, _  = self.cache_data.popitem()
                print(f"DISCARD: {discard_key}")
            elif key in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key = key
                del self.cache_data[key]
                #print(f"DISCARD: {discard_key}")
            self.cache_data[key] = item

    def get(self, key):
        """Gets value equivalent to a key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
