#!/usr/bin/env python3
"""A script for implementing caching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic cache"""
    def __init__(self):
        """Instantiate attributes of the class BasicCache"""
        super().__init__()

    def put(self, key, item):
        """Assign value to the key"""
        if key is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get the value linked to a key"""
        return self.cache_data.get(key, None)
