

mem_map = {}

perm_set = []


def insert(array, value):
    p_set = []
    for i in range(len(array) + 1):
        p = array[:]
        p.insert(i, value)
        p_set.append(p)
    return p_set


def find_permutation(array):
    if len(array) <= 1:
        return array
    elif len(array) == 2:
        return array, [array[1], array[0]]
    else:
        result = []
        for each in find_permutation(array[:-1]):
            result.extend(insert(each, array[-1]))
    return result


class Solution(object):
    PERMUTATIONS = []
    CURRENT_KEY = 0
    CURRENT_SHUFFLE = None

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.PERMUTATIONS = find_permutation(nums)
        self.CURRENT_SHUFFLE = nums
        self.CURRENT_KEY = 0

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.CURRENT_SHUFFLE = self.nums
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
    # result = find_permutation([1, 2])
    # print result, len(result)
    # result = find_permutation([1, 2, 3])
    # print result, len(result)
    # result = find_permutation([1, 2, 3, 4])
    # print result, len(result)
    # result = find_permutation([1, 2, 3, 4, 5])
    # print result, len(result)
    result = find_permutation([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    print result, len(result)
    # obj = Solution([1, 2])
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
    # obj = Solution([])
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

    # obj = Solution([1,2,3,4,5,6,7,8,9,10,11,12])
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
