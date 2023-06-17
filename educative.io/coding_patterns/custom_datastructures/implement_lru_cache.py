"""
Implement an LRU cache class with the following functions:

Init(capacity): Initializes an LRU cache with the capacity size.
Set(key, value): Adds a new key-value pair or updates an existing key with a new value.
Get(key): Returns the value of the key, or -1 if the key does not exist.

If the number of keys has reached the cache capacity, evict the least recently used key and then add the new key.

As caches use relatively expensive, faster memory, they are not designed to store very large data sets. Whenever the cache becomes full, we need to evict some data from it. There are several caching algorithms to implement a cache eviction policy. LRU is a very simple and commonly used algorithm. The core concept of the LRU algorithm is to evict the oldest data from the cache to accommodate more data.

"""


from collections import deque

# Tip: You may use some of the code templates provided
# in the support files

# We will use a linkedlist of a pair of integers
# where the first integer will be the key
# and the second integer will be the value


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_map = {}
        self.deque = []

    def update_key_usage(self,key, exists=False):
        if exists:
            key_idx = self.deque.index(key)
            self.deque.remove(key)
        self.deque.append(key)

    def get(self, key):
        # if key exists return the value and update the deque
        if key not in self.cache_map:
            return -1
        result = self.cache_map[key]
        self.update_key_usage(key, exists=True)
        return result

    def set(self, key, value):
        if key in self.cache_map:
            self.cache_map[key] = value
            self.update_key_usage(key, exists=True)
        else:
            # check the capacity and evict if required
            if len(self.cache_map) == self.capacity:
                del self.cache_map[self.deque.pop(0)]
            self.cache_map[key] = value
            self.update_key_usage(key, exists=False)
    
    def print(self):
        print("Cache current size: ", len(self.deque),
              ", ", end="")
        print("Cache contents:", end="")

        print(self.deque)
        print("-"*100, "\n")
    

def main():
    # Creating a cache of size 2
    cache_capacity = 2
    cache = LRUCache(cache_capacity)
    print("Initial state of cache")
    print("Cache capacity: " + str(cache_capacity))
    cache.print()

    keys = [10, 10, 15, 20, 15, 25, 5]
    values = ["20", "get", "25", "40", "get", "85", "5"]

    for i in range(len(keys)):
        if values[i] == "get":
            print("Getting by Key: ", keys[i])
            print("Cached value returned: ", cache.get(keys[i]))
        else:
            print("Setting cache: Key: ", keys[i], ", Value: ", values[i])
            cache.set(keys[i], int(values[i]))
        cache.print()


if __name__ == '__main__':
    main()

