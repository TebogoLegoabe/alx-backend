#!/usr/bin/python3
"""Create MRUCache class that inherits from BaseCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """A caching system with LFU eviction"""

    def __init__(self):
        """ Initialize MRUCache """
        self.stack = []
        super().__init__()

    def put(self, key, item):
        """
        Store an item in the cache.

        Args:
            key: The key to store the item under.
            item: The item to store.
        """
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                delete = self.stack.pop()
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key, or None if the key is not found.
        """
        if self.cache_data.get(key):
            self.stack.remove(key)
            self.stack.append(key)
        return self.cache_data.get(key)