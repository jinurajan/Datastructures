"""
Longest Arithmetic Subsequence
Given an array A of integers, return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).



Example 1:

Input: A = [3,6,9,12]
Output: 4
Explanation:
The whole array is an arithmetic sequence with steps of length = 3.
Example 2:

Input: A = [9,4,7,2,10]
Output: 3
Explanation:
The longest arithmetic subsequence is [4,7,10].
Example 3:

Input: A = [20,1,15,3,10,5,8]
Output: 4
Explanation:
The longest arithmetic subsequence is [20,15,10,5].

Constraints:

2 <= A.length <= 1000
0 <= A[i] <= 500

"""
from typing import List

class Solution1:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) < 2:
            return len(A)
        max_len = 0

        def find_consec_aps(start_idx, diff, current):
            hash_set = set(A[start_idx:])
            next_val = current +diff
            count = 0
            while next_val in hash_set:
                count += 1
                next_val += diff
            return count
        for i in range(len(A)):
            for j in range( i+1, len(A)):
                ap_count = find_consec_aps( j +1, A[j ] -A[i], A[j])
                max_len = max(max_len, ap_count +2)
        return max_len

from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        import pdb; pdb.set_trace()
        ans = 0
        cnt = defaultdict(lambda: 1)
        seen = set()
        for x in A:
            for xx in seen:
                cnt[x, x-xx] = 1 + cnt[xx, x-xx]
                ans = max(ans, cnt[x, x-xx])
            seen.add(x)
        return ans


# A = [3,6,9,12]
# print(Solution().longestArithSeqLength(A))

A = [9,4,7,2,10]
print(Solution().longestArithSeqLength(A))

A = [20,1,15,3,10,5,8]
print(Solution().longestArithSeqLength(A))

A = [12,28,13,6,34,36,53,24,29,2,23,0,22,25,53,34,23,50,35,43,53,11,48,56,44,53,31,6,31,57,46,6,17,42,48,28,5,24,0,14,43,12,21,6,30,37,16,56,19,45,51,10,22,38,39,23,8,29,60,18]
print(Solution().longestArithSeqLength(A))
