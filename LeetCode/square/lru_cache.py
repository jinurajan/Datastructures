"""
LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        try:
            self.cache.move_to_end(key)
            return self.cache[key]
        except KeyError:
            return -1
        

    def put(self, key: int, value: int) -> None:
        try:
            self.cache.move_to_end(key)
            self.cache[key] = value
        except KeyError:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)