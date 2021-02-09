"""
LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?


Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); # cache is {1=1}
lRUCache.put(2, 2); # cache is {1=1, 2=2}
lRUCache.get(1);    # return 1
lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    # returns -1 (not found)
lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    # return -1 (not found)
lRUCache.get(3);    # return 3
lRUCache.get(4);    # return 4

Constraints:

1 <= capacity <= 3000
0 <= key <= 3000
0 <= value <= 104
At most 3 * 104 calls will be made to get and put.

"""
from collections import deque, OrderedDict


class LRUCache1:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.Q = deque()

    def get(self, key: int) -> int:
        try:
            ret = self.cache[key]
            self.Q.remove(key)
            self.Q.append(key)
            return ret
        except KeyError:
            return  -1

    def put(self, key: int, value: int) -> None:
        try:
            self.cache[key]
            self.cache[key] = value
            self.Q.remove(key)
            self.Q.append(key)
        except KeyError:
            if len(self.cache) == self.capacity:
                del self.cache[self.Q.popleft()]
            self.cache[key] = value
            self.Q.append(key)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        try:
            self.cache.move_to_end(key)
            return self.cache[key]
        except KeyError:
            return  -1

    def put(self, key: int, val: int) -> None:
        try:
            self.cache.move_to_end(key)
            self.cache[key] = val
        except KeyError:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = val





# lRUCache = LRUCache(2)
# lRUCache.put(1, 1)
# print(lRUCache.cache, lRUCache.Q)# cache is {1=1}
# lRUCache.put(2, 2) # cache is {1=1, 2=2}
# print(lRUCache.cache, lRUCache.Q)
# lRUCache.get(1)    # return 1
# print(lRUCache.cache, lRUCache.Q)
# lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# print(lRUCache.cache, lRUCache.Q)
# lRUCache.get(2)    # returns -1 (not found)
# print(lRUCache.cache, lRUCache.Q)
# lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# print(lRUCache.cache, lRUCache.Q)
# lRUCache.get(1)    # return -1 (not found)
# print(lRUCache.cache, lRUCache.Q)
# lRUCache.get(3)    # return 3
# print(lRUCache.cache, lRUCache.Q)
# lRUCache.get(4)    # return 4

import pdb; pdb.set_trace()
lru_cache = LRUCache(2)
lru_cache.put(2, 1)
lru_cache.put(2, 2)
lru_cache.get(2)
lru_cache.put(1, 1)
lru_cache.put(4, 1)
lru_cache.get(2)


