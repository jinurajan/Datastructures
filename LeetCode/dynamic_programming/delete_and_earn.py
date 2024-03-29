"""
Delete and Earn

You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

 

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
"""
from collections import Counter, defaultdict
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points, prev, curr = Counter(nums), 0, 0
    
        for value in range(max(points.keys()) + 1):
            prev, curr = curr, max(prev + value * points[value], curr)
        return curr


class Solution1(object):
    def deleteAndEarn(self, nums):
        points, prev, curr = Counter(nums), 0, 0
        for value in range(10001):
            prev, curr = curr, max(prev + value * points[value], curr)
        return curr

class Solution2:
    def rob(self, nums):
        prev, curr = 0, 0
        for value in nums:
            prev, curr = curr, max(prev+value, curr)
        return curr

    def deleteAndEarn(self, nums: List[int]) -> int:
        points = [0]*10001
        for num in nums:
            points[num] += num
        return self.rob(points)

class Solution3(object):
    def deleteAndEarn(self, nums):
        points, prev, curr = [0] * 10001, 0, 0
        for num in nums:
            points[num] += num
        for value in points:
            prev, curr = curr, max(prev + value, curr)
        return curr

class Solution4:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
        
        two_back = 0
        one_back = points[1]
        for num in range(2, max_number+1):
            two_back, one_back = one_back, max(one_back, two_back+points[num])
        return one_back
        


class Solution5:
    # TLE -> Time limit exceeded
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = Counter(nums)
        for num,val in points.items():
            points[num] = num*val
        max_number = max(points)
        def max_points(n):
            if n == 0:
                return 0
            if n == 1:
                return points[1]
            return max(max_points(n-1), max_points(n-2)+points[n])
        return max_points(max_number)
        