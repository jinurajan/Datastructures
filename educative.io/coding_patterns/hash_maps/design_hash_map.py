"""
Design a hash map without using the built-in libraries. We only need to cater integer keys and integer values in the hash map. Return NULL if the key doesn’t exist.

It should support the following three primary functions of a hash map:

Put(key, value): This function inserts a key and value pair into the hash map. If the key is already present in the map, then the value is updated. Otherwise, it is added to the bucket.

Get(key): This function returns the value to which the key is mapped. It returns -1
, if no mapping for the key exists.

Remove(key): This function removes the key and its mapped value.

"""


# A class implementation of the bucket data structure
class Bucket:
    # Initialize bucket here
    def __init__(self):
        self.bucket = []
    
    # get value from bucket
    def get(self, key):
        # Write - Your - Code
        for (k,v) in self.bucket:
            if k == key:
                return v
        return -1

    # put value in bucket
    def update(self, key, value):
        # Write - Your - Code
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))

    # delete value from bucket
    def remove(self, key):
        # Write - Your - Code
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]

class MyHashMap():
    # Use the constructor below to initialize the hashmap based on the keyspace
    def __init__(self, key_space):
        # Write your code here
        self.key_space = key_space
        self.buckets = [Bucket()] * key_space

    def put(self, key, value):
        # Write your code here
        if key is None or value is None:
            return
        hash_key = key % self.key_space
        self.buckets[hash_key].update(key, value)

    def get(self, key):
        # Write your code here
        if key is None:
            return -1
        hash_key = key % self.key_space
        return self.buckets[hash_key].get(key)

    def remove(self, key):
        # Write your code here
        hash_key = key % self.key_space
        self.buckets[hash_key].remove(key)
