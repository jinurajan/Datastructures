

mem_map = {}

perm_set = []


def insert(array, value):
    p_set = []
    for i in range(len(array) + 1):
        p = array[:]
        p.insert(i, value)
        p_set.append(p)
    return p_set


def find_permutation_with_replacement(array):
    if len(array) <= 1:
        return array
    elif len(array) == 2:
        return array, [array[1], array[0]]
    else:
        result = []
        for each in find_permutation_with_replacement(array[:-1]):
            result.extend(insert(each, array[-1]))
    return result


def toInteger(List): 
    return [int(i) for i in List]


def find_permutations(a, l, r):
    if l == r:
        # reached the end of the string
        perm_set.append(toInteger(a))
    else:
        for i in xrange(l, r+1):
            a[l], a[i] = a[i], a[l]
            find_permutations(a, l+1, r)
            a[l], a[i] = a[i], a[l]


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        # making integer to string for immutability
        self.PERMUTATIONS = []
        self.find_permutations([str(i) for i in nums], 0, len(nums)-1)
        self.CURRENT_SHUFFLE = nums
        self.CURRENT_KEY = 0

    def toInteger(self, List): 
        return [int(i) for i in List]

    def find_permutations(self, a, l, r):
        if l == r:
            # reached the end of the string
            self.PERMUTATIONS.append(self.toInteger(a))
        else:
            for i in xrange(l, r+1):
                a[i], a[l] = a[l], a[i]
                self.find_permutations(a, l+1, r)
                a[i], a[l] = a[l], a[i]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        # self.CURRENT_SHUFFLE = self.nums
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        if not self.PERMUTATIONS:
            return self.nums
        perm = self.PERMUTATIONS[self.CURRENT_KEY]
        if perm != self.CURRENT_SHUFFLE:
            self.update_current_key()
            self.CURRENT_SHUFFLE = perm
            return self.CURRENT_SHUFFLE
        else:
            self.update_current_key()
            self.CURRENT_SHUFFLE = self.PERMUTATIONS[self.CURRENT_KEY]
            return self.CURRENT_SHUFFLE

    def update_current_key(self):
        self.CURRENT_KEY += 1
        if self.CURRENT_KEY > len(self.PERMUTATIONS) - 1:
            self.CURRENT_KEY = 0


if __name__ == "__main__":
    # find_permutations([1, 2], 0, 1)
    # print perm_set
    # result = find_permutation([1, 2, 3])
    # print result, len(result)
    # result = find_permutation([1, 2, 3, 4])
    # print result, len(result)
    # result = find_permutation([1, 2, 3, 4, 5])
    # print result, len(result)
    # result = find_permutation([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    # print result, len(result)
    # obj1 = Solution([1, 2])
    # obj1.PERMUTATIONS, obj1.CURRENT_KEY, obj1.CURRENT_SHUFFLE
    # print "shuffle1:{}".format(obj1.shuffle())
    # print "shuffle2:{}".format(obj1.shuffle())
    # print "shuffle3:{}".format(obj1.shuffle())
    # print "reset1:{}".format(obj1.reset())
    # print "shuffle1:{}".format(obj1.shuffle())
    # print "shuffle2:{}".format(obj1.shuffle())
    # print "shuffle3:{}".format(obj1.shuffle())
    # print "shuffle4:{}".format(obj1.shuffle())
    # print "shuffle5:{}".format(obj1.shuffle())
    # print "reset2:{}".format(obj1.reset())
    # print "shuffle6:{}".format(obj1.shuffle())
    # print "******************************"
    # obj2 = Solution([1, 2, 3])
    # obj2.PERMUTATIONS, obj2.CURRENT_KEY, obj2.CURRENT_SHUFFLE
    # print "shuffle1:{}".format(obj2.shuffle())
    # print "shuffle2:{}".format(obj2.shuffle())
    # print "shuffle3:{}".format(obj2.shuffle())
    # print "reset1:{}".format(obj2.reset())
    # print "shuffle1:{}".format(obj2.shuffle())
    # print "shuffle2:{}".format(obj2.shuffle())
    # print "shuffle3:{}".format(obj2.shuffle())
    # print "shuffle4:{}".format(obj2.shuffle())
    # print "shuffle5:{}".format(obj2.shuffle())
    # print "reset2:{}".format(obj2.reset())
    # print "shuffle6:{}".format(obj2.shuffle())
    # print "******************************"
    # obj = Solution([1, 2, 3, 4, 5])
    # obj.PERMUTATIONS, obj.CURRENT_KEY, obj.CURRENT_SHUFFLE
    # print "shuffle1:{}".format(obj.shuffle())
    # print "shuffle2:{}".format(obj.shuffle())
    # print "shuffle3:{}".format(obj.shuffle())
    # print "reset1:{}".format(obj.reset())
    # print "shuffle1:{}".format(obj.shuffle())
    # print "shuffle2:{}".format(obj.shuffle())
    # print "shuffle3:{}".format(obj.shuffle())
    # print "shuffle4:{}".format(obj.shuffle())
    # print "shuffle5:{}".format(obj.shuffle())
    # print "reset2:{}".format(obj.reset())
    # print "shuffle6:{}".format(obj.shuffle())
    obj = Solution([1, 2, 3])
    print obj.PERMUTATIONS
    print "shuffle1:{}".format(obj.shuffle())
    print "reset1:{}".format(obj.reset())
    print "shuffle2:{}".format(obj.shuffle())
