"""
Given set of N integers find the triples where sum of triples are 0
"""


class Threesum(object):
    """
        O(N3)
    """
    def count(self, nums):
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        count += 1
        return count


class ThreesumOptimized(object):
    """
        O(N2 logn)
        sort using Nlogn
        two loops = N2 * logN for searching

        NlogN + N2 logN ~ N2logN

    """
    def binary_search(self, nums, k, l, r):
        if l <= r:
            mid = (l + r) / 2
            if nums[mid] == k:
                return mid
            if nums[mid] > k:
                return self.binary_search(nums, k, l, mid-1)
            else:
                return self.binary_search(nums, k, mid+1, r)
        return -1

    def count(self, nums):
        n = len(nums) 
        nums = sorted(nums)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                key = -(nums[i] + nums[j])
                index = self.binary_search(nums, key, 0, n-1)
                if index != -1 and nums[i] < nums[j] and nums[j] < nums[index]:
                    count += 1
        return count






print Threesum().count([30, -40, -20, -10, 40, 0, 10, 5])
print ThreesumOptimized().count([30, -40, -20, -10, 40, 0, 10, 5])