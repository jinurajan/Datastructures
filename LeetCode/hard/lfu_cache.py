"""
LFU Cache
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.


Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[3,4], cnt(4)=2, cnt(3)=3


Constraints:

0 <= capacity, key, value <= 104
At most 105 calls will be made to get and put.


Follow up: Could you do both operations in O(1) time complexity?

"""
from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.minFreq = 1
        self.keyMap = defaultdict()
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

lfu_cache = LFUCache(2)
lfu_cache.put(1, 1)
lfu_cache.put(2, 2)
lfu_cache.get(1)
lfu_cache.put(3, 3)
lfu_cache.get(2)
lfu_cache.get(3)
lfu_cache.put(4, 4)
lfu_cache.get(1)
lfu_cache.get(3)
lfu_cache.get(4)





