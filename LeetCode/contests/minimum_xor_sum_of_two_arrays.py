"""
Minimum XOR Sum of Two Arrays
You are given two integer arrays nums1 and nums2 of length n.

The XOR sum of the two integer arrays is (nums1[0] XOR nums2[0]) + (nums1[1] XOR nums2[1]) + ... + (nums1[n - 1] XOR nums2[n - 1]) (0-indexed).

For example, the XOR sum of [1,2,3] and [3,2,1] is equal to (1 XOR 3) + (2 XOR 2) + (3 XOR 1) = 2 + 0 + 2 = 4.
Rearrange the elements of nums2 such that the resulting XOR sum is minimized.

Return the XOR sum after the rearrangement.



Example 1:

Input: nums1 = [1,2], nums2 = [2,3]
Output: 2
Explanation: Rearrange nums2 so that it becomes [3,2].
The XOR sum is (1 XOR 3) + (2 XOR 2) = 2 + 0 = 2.
Example 2:

Input: nums1 = [1,0,3], nums2 = [5,3,4]
Output: 8
Explanation: Rearrange nums2 so that it becomes [5,4,3].
The XOR sum is (1 XOR 5) + (0 XOR 4) + (3 XOR 3) = 4 + 4 + 0 = 8.


Constraints:

n == nums1.length
n == nums2.length
1 <= n <= 14
0 <= nums1[i], nums2[i] <= 107

"""


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        cache = {}
        dp = [1 for _ in range(len(nums2))]

        def find_min_xor_sum(dp, index):
            if index == len(nums2):
                return 0
            key = "{}-{}".format(index, tuple(dp))
            if key not in cache:
                min_sum = float("inf")
                for j in range(len(dp)):
                    if dp[j] == 0:
                        continue
                    dp[j] = 0
                    min_sum = min(min_sum, (nums1[index] ^ nums2[j]) + find_min_xor_sum(dp, index + 1))
                    dp[j] = 1
                cache[key] = min_sum
            return cache[key]

        return find_min_xor_sum(dp, 0)

