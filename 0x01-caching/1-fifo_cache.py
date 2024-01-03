#!/usr/bin/env python3
"""FIFO cathing"""
BaseCaching = __import__('base_caching').BaseCaching
class FIFOCache(BaseCaching):
    """
    A caching system with FIFO eviction.
    """

    def __init__(self):
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        Store an item in the cache.

        Args:
            key: The key to store the item under.
            item: The item to store.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_order.append(key)
            if len(self.cache_order) > self.MAX_ITEMS:
                discarded_key = self.cache_order.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key, or None if the key is not found.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
