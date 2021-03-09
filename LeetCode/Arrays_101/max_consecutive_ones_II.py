"""
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

"""
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_ones = 0
        prev_count = 0
        for i, num in enumerate(nums):
            if num == 0:
                max_ones = max(max_ones, count+prev_count+1)
                prev_count = count
                count = 0
            else:
                count += 1
        if max_ones == 0:
            return count
        return max(max_ones, count+prev_count+1)

class Solution1:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """ sliding window """
        longest_seq = 0
        left, right = 0, 0
        num_zeros = 0
        while right < len(nums):
            if nums[right] == 0:
                num_zeros += 1
            while num_zeros == 2:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1
            longest_seq = max(longest_seq, right-left+1)
            right += 1
        return longest_seq



nums = [1]
print(Solution().findMaxConsecutiveOnes(nums))

nums = [0, 1]
print(Solution().findMaxConsecutiveOnes(nums))

nums = [1,0,1,1,0]
print(Solution().findMaxConsecutiveOnes(nums))

nums = [1,1, 0, 1]
print(Solution().findMaxConsecutiveOnes(nums))

nums = [1,0,1,1,0,1]
print(Solution().findMaxConsecutiveOnes(nums))

nums = [0, 1]
print(Solution().findMaxConsecutiveOnes(nums))

nums = []
print(Solution().findMaxConsecutiveOnes(nums))

nums = [1,1,0,1, 1, 1, 1]
print(Solution().findMaxConsecutiveOnes(nums))



