"""
Contains Duplicate III

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false

"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        n = len(nums)
        if t == 0 and len(set(nums)) == n:
            # no duplicates
            return False
        for idx, val in enumerate(nums):
            for j in range(idx+1, min(idx+1+k, len(nums))):
                if abs(val - nums[j]) <= t:
                    return True

        return False


def search(array, val, t):
    for each in array:
        if abs(val - each) <= t:
            return True
    return False


class Solution2(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        n = len(nums)
        for i in range(n):
            print i,
            poss_arrays = []
            if i - k < 0:
                poss_arrays.append(nums[:i])
            else:
                poss_arrays.append(nums[i - k:i])
            if i + k > n:
                poss_arrays.append(nums[i + 1:])
            else:
                poss_arrays.append(nums[i + 1: i + k + 1])
            print "possible arrays to search for {} is {} and {}".format(
                nums[i], poss_arrays[0], poss_arrays[1])
            # if search(poss_arrays[0], nums[i], t) or search(poss_arrays[1], nums[i], t):
            #     return True

        return False


def bin_search(array, l, r, val):
    if l == r:
        # only one element
        if array[l] <= val:
            return True
    if l < r:
        mid = (l + (r - l)) // 2
        if array[mid] <= val:
            return True
        else:
            return bin_search(array, l, mid, val)
    return False


class Solution1(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        val = False
        for i in range(len(nums)):
            print "nums:{} k: {} t: {}".format(nums, k, t),
            pos_array_1 = nums[i-k:i-1] if i-k >= 0 else nums[0:i-1]
            pos_array_2 = nums[i+1: i+k+1]
            arrays_to_be_checked = []
            print "nums[i]:{} pos_array_1:{} pos_array_2:{}".format(nums[i], pos_array_1, pos_array_2)
            if pos_array_1:
                arrays_to_be_checked.append(sorted(pos_array_1))
            if pos_array_2:
                arrays_to_be_checked.append(sorted(pos_array_2))
            if not arrays_to_be_checked:
                return False
            for array in arrays_to_be_checked:
                print("{} checked for {} in {} == {}".format(nums[i], nums[i]+t, array, bin_search(array, 0, len(array)-1, nums[i]+t)))
                print("{} checked for {} in {} == {}".format(nums[i], nums[i]-t, array, bin_search(array, 0, len(array)-1, nums[i]-t)))
                if bin_search(array, 0, len(array)-1, nums[i]+t) or bin_search(array, 0, len(array)-1, nums[i]-t):
                    val = True
                    break
        return val


print Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0) == True

print Solution().containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2) == True

print Solution().containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3) == False

print Solution().containsNearbyAlmostDuplicate([-1, -1], 1, -1) == False
