#!/usr/bin/env python3
"""A script that implements MRU caching system"""

BaseCaching = __import__('0-basic_cache').BaseCaching


class MRUCache(BaseCaching):
    """An MRUCache class"""
    def __init__(self):
        """Instantiate atrribute of class"""
        self.last_accessed_key = None
        super().__init__()

    def put(self, key, item):
        """Loads the dict with kay: value"""
        if key is not None and item is not None:
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key = self.last_accessed_key
                if discard_key in self.cache_data:
                    del self.cache_data[discard_key]
                    print(f"DISCARD: {discard_key}")
                elif discard_key not in self.cache_data and \
                    len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    discard_key, _ = self.cache_data.popitem()
                    print(f"DISCARD: {discard_key}")
            self.cache_data[key] = item

    def get(self, key):
        """Assigns value to a key"""
        if key is None or key not in self.cache_data:
            return None
        self.last_accessed_key = key
        return self.cache_data[key]
