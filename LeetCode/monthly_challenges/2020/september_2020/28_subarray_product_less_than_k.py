"""
Subarray Product Less Than K

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""
class Solution1(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        O(N2)
        """
        total = 0
        i = 0
        while i < len(nums):
            j = 0
            while i+j < len(nums):
                if reduce(lambda x, y: x*y, nums[i:i+j+1]) >= k:
                    break
                else:
                    total += 1
                j += 1
            i += 1
        return total


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        10, 5, 2, 6
        
        left = 0
        count = 0
        product = 1
        loop 1
        ------
        right = 0
        val = 10
        product = 1*10 = 10
        product ! > k
        count += 0 - 0 + 1
        count = 1

        loop 2
        ------
        right  = 1
        val = 5
        product = 10*5 = 50
        product ! > k
        count = 1 + (1 - 0) + 1 = 3

        loop 3
        ------
        right = 2
        val = 2
        product = 100
        while loop 
            product = 100 / 10 = 10
            left = 1
        product < k
        count = 3 + (2-1)+ 1 = 5
        loop 4
        ------
        right = 3
        val = 6
        product = 60

        count = 5 + (3-1) + 1 = 5 + 2 + 1 = 8

        """
        import pdb; pdb.set_trace()
        left = count = 0
        product = 1
        for right, val in enumerate(nums):
            product *= val
            while  product >= k and left < right:
                product /= nums[left]
                left += 1
            if product < k:
                count += right - left + 1
        return count





print Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100)