#!/usr/bin/env python3
"""Basic dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching
class BasicCache(BaseCaching):
   """
   A caching system with no limit.
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
