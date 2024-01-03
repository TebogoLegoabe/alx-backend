#!/usr/bin/env python3
"""FIFO cathing"""


BaseCaching = __import__('base_caching').BaseCaching
class LIFOCache(BaseCaching):
    """
    A caching system with LIFO eviction.
    """

    def put(self, key, item):
        """
        Store an item in the cache.

        Args:
            key: The key to store the item under.
            item: The item to store.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discarded_key = list(self.cache_data)[-1]  # Get the most recently added key
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
