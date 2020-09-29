"""

"""

class Solution1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid -1
            else:
                l = mid + 1
        return -1


class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def binary_search(nums, l, r, key):
            if l <= r:
                mid = (l + r) / 2
                if nums[mid] == key:
                    return mid
                elif nums[mid] > key:
                    return binary_search(nums, l, mid - 1, key)
                else:
                    return binary_search(nums, mid + 1, r, key)
            return -1
        return binary_search(nums, 0,len(nums)-1, target)


class Solution3(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def binary_search(nums, l, r, key):
            if l < r:
                mid = l + (r-l) / 2
                if nums[mid] == key:
                    return mid
                elif nums[mid] > key:
                    return binary_search(nums, l, mid - 1, key)
                else:
                    return binary_search(nums, mid + 1, r, key)
            return -1
        return binary_search(nums, 0, len(nums)-1, target)

print Solution1().search([1,2,3,4,5,6,7], 6)
print Solution2().search([1,2,3,4,5,6,7], 6)
print Solution3().search([1,2,3,4,5,6,7], 6)