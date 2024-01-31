#!/usr/bin/env python3
"""A script that implements MRU caching system"""

BaseCaching = __import__('0-basic_cache').BaseCaching


class LFUCache(BaseCaching):
    """An MRUCache class"""
    def __init__(self):
        """Instantiate atrribute of class"""
        super().__init__()
        self.last_accessed_key = None
        self.frequency = {}

    """def put(self, key, item):
        Loads the dict with kay: value
        used_once = []
        if key is not None or item is not None:
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                get_key = self.last_accessed_key
                used_once.append(get_key)
                discard_key = list(self.cache_data.keys())[0]
                del self.cache_data[discard_key]
                print(f"DISCARD: {discard_key}")

            for k in used_once:
                print(f"Key is: {k}")
            self.cache_data[key] = item"""
    def put(self, key, item):
        """Loads the dict with kay: value"""
        if key is not None and item is not None:
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS: 
                if self.last_accessed_key in self.cache_data:
                    self.frequency[self.last_accessed_key] += 1

                least_freq_key = min(self.frequency, key=lambda k: self.frequency[k])
                del self.cache_data[least_freq_key]
                del self.frequency[least_freq_key]
                print(f"DISCARD: {least_freq_key}")

            self.frequency[key] = self.frequency.get(key, 0) +1
            self.cache_data[key] = item

    def get(self, key):
        """Assigns value to a key"""
        if key is None or key not in self.cache_data:
            return None
        self.last_accessed_key = key
        self.frequency[key] += 1
        return self.cache_data[key]
