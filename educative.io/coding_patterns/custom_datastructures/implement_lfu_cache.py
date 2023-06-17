"""
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class. Here is how it should be implemented:

LFUCache(capacity): This function initializes the object with the capacity of the data structure.

Get(key): This function gets the value of the key if it exists in the cache. Otherwise, it returns -1.

Put(key, value): This function updates the value of the key if present, or inserts the key if it’s not present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there’s a tie, that is, two or more keys have the same frequency, the least recently used key is invalidated.


To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key. When a key is first inserted into the cache, its use counter is set to 1 (due to the Put() operation). The use counter for a key in the cache is incremented and either a Get() or Put() operation is called on it.


The Get() and Put() functions should both run with an average time complexity of O(1).


"""

from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.minFreq = 1
        # {'a': 1}
        self.keyMap = defaultdict()
        # {3: {a: b, b:c}, 4: {d:e}}
        self.freqMap = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if not self.keyMap or \
                key not in self.keyMap:
            return -1
        # get curr freq
        freq = self.keyMap[key]

        # read value
        val = self.freqMap[freq][key]

        # bump up frequency
        self.freqMap[freq + 1][key] = val
        self.keyMap[key] = freq + 1

        # delete old entry
        del self.freqMap[freq][key]

        # if old freq has 0 elements,
        # and oldFreq==minFreq, +1 minFreq
        if not self.freqMap[self.minFreq]:
            self.minFreq += 1

        return val

    def put(self, key: int, value: int) -> None:
        print('put:%u,%u' % (key, value))
        if not self.cap:  # capacity=0
            return
        if key not in self.keyMap:
            if self.size == self.cap:
                # evict first node of lowest frequency
                lfuKey, _ = self.freqMap[self.minFreq].popitem(0)
                del self.keyMap[lfuKey]
                self.size -= 1
            # create new entry of freq 1
            self.keyMap[key] = 1
            self.freqMap[1][key] = value
            # minFreq is always 1 when new
            # elements are inserted
            self.minFreq = 1
            self.size += 1

        else:  # update existing key
            freq = self.keyMap[key]
            # write new value to oldFreq+1
            self.freqMap[freq + 1][key] = value
            # bump up frequency of this key
            del self.freqMap[freq][key]
            self.keyMap[key] += 1
            # same as in get
            # if oldFreq is empty AND eq minFreq, increment
            if not self.freqMap[self.minFreq]:
                self.minFreq += 1
        return