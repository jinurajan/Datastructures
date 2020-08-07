"""
Design HashSet
Design a HashSet without using any built-in hash table libraries.

To be specific,  your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet,  do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0,  1000000].
The number of operations will be in the range of [1,  10000].
Please do not use the built-in HashSet library.

"""
from sys import getsizeof


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.int_size = getsizeof(1)
        array_size = 1000000 // self.int_size
        self.hash = [0] * array_size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key // self.int_size
        self.hash[index] |= 1 << (self.int_size - (key % self.int_size))

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            index = key // self.int_size
            self.hash[index] ^= 1 << (self.int_size - (key % self.int_size))

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        index = key // self.int_size
        if self.hash[index] & (1 << (self.int_size - (key % self.int_size))):
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
if __name__ == "__main__":
    # hashSet = MyHashSet();
    # hashSet.add(1)
    # hashSet.add(2)
    # print hashSet.contains(1)
    # print hashSet.contains(3)
    # hashSet.add(2)
    # print hashSet.contains(2)
    # hashSet.remove(2)
    # print hashSet.contains(2)
    hashSet = MyHashSet()
    given_outputs = [None, None, None, None, False, None, None, None, None, False, None, None, None, None, None, None, None, None, None, None, None, None, True, None, None, None, None, None, None, None, None, None, None, None, None, None, None, False, True, None, None, None, None, None, None, None, True, True, None, None, None, None, None, None, True, None, None, None, None, None, None, None, None, None, None, None, False, None, None, None, None, None, None, None, None, True, None, None, None, None, None, None, None, True, True, None, None, False, None, None, None, None, None, True, True, None, None, None, None, None]
    input_oper = ["remove", "remove", "add", "add", "contains", "add", "add", "add", "remove", "contains", "add", "add", "add", "remove", "add", "remove", "add", "add", "add", "remove", "add", "remove", "contains", "add", "add", "add", "add", "add", "add", "add", "remove", "remove", "remove", "add", "add", "remove", "add", "contains", "contains", "add", "remove", "add", "add", "add", "add", "add", "contains", "contains", "add", "add", "add", "add", "add", "remove", "contains", "remove", "add", "add", "add", "add", "add", "remove", "add", "add", "add", "add", "contains", "add", "add", "add", "add", "add", "remove", "add", "add", "contains", "add", "add", "add", "remove", "remove", "remove", "remove", "contains", "contains", "add", "add", "contains", "add", "add", "add", "add", "add", "contains", "contains", "add", "remove", "add", "remove", "add"]
    input_val = [[88], [56], [17], [20], [83], [43], [27], [20], [21], [15], [90], [69], [95], [12], [60], [78], [94], [85], [70], [45], [84], [89], [17], [12], [47], [26], [90], [26], [63], [88], [83], [51], [10], [71], [85], [38], [1], [87], [27], [26], [30], [44], [39], [89], [54], [18], [84], [94], [63], [41], [77], [31], [9], [76], [85], [80], [6], [85], [13], [89], [49], [12], [35], [81], [32], [75], [48], [33], [33], [0], [6], [97], [3], [94], [90], [9], [87], [68], [32], [3], [85], [13], [89], [18], [78], [57], [47], [85], [94], [53], [14], [12], [62], [44], [31], [10], [69], [48], [38], [54]]
    outputs = []
    for i in range(len(input_oper)):
        if input_oper[i] == "remove":
            print "remove",
            op = hashSet.remove(input_val[i][0])
        elif input_oper[i] == "add":
            print "add",
            op = hashSet.add(input_val[i][0])
        else:
            print "contains",
            op = hashSet.contains(input_val[i][0])
        outputs.append(op)
    print outputs
