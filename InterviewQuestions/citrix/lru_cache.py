# This is Python 2
import sys


class LRUCache(object):
    def __init__(self):
        self.cache = {}
        self.exit = False
        self.timeline_entry = []

    def add(self, key, val):
        if not self.exit:
            self.cache[key] = val
            # update the timeline_entry
            self.timeline_entry.append(key)
        else:
            raise Exception("LRU Cache is exited")

    def get(self, key):
        try:
            return self.cache[key]
        except KeyError:
            return -1

    def remove(self, key):
        try:
            val = self.cache[key]
            del self.cache[key]
            return val
        except KeyError:
            return -1

    def exit_cache(self):
        # using name exit_cache as exit is python keyword
        self.exit = True

    def evict(self):
        if self.timeline_entry:
            key = self.timeline_entry.pop(-1)
            self.cache.pop(key)
        else:
            raise Exception("LRU Cache is Empty")

line = ""
lru_cache = LRUCache()
outputs = []
while line != "exit":
    line = sys.stdin.readline()
    line = line.strip()
    raw_inputs = line.split(" ")
    command = raw_inputs[0].strip()
    inputs = [int(i) for i in raw_inputs[1:]]
    if command == "exit":
        for each in outputs:
            print each
        break
    if command == "add":
        lru_cache.add(inputs[0], inputs[1])
    elif command == "get":
        outputs.append(lru_cache.get(inputs[0]))
    elif command == "evict":
        lru_cache.evict()
    elif command == "remove":
        outputs.append(lru_cache.remove(inputs[0]))


# if __name__ == "__main__":
#     a = LRUCache()
#     a.add(5, 3)
#     a.add(1, 2)
#     print a.get(5)
#     a.evict()
#     print a.get(1)
#     print a.remove(5)
#     a.exit
