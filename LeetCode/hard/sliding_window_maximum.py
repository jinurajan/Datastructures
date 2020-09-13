"""
239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < k:
            return []
        elif k == 1:
            return nums
        elif len(nums) == k:
            return [max(nums)]
        else:
            max_val = max(nums[:k])
            res = [max_val]
            for i in range(1, len(nums) - k + 1):
                if max_val == nums[i-1]:
                    # need to find max in rest of the k-1 elements
                    max_val = max(nums[i:i+k])
                else:
                    max_val = max(max_val, nums[i+k-1])
                res.append(max_val)
            return res

print Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == 
print Solution().maxSlidingWindow([1, -1], 1)
