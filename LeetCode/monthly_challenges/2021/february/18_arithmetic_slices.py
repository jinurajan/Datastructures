"""
Arithmetic Slices

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of the array A is called arithmetic if the sequence:
A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

"""
from typing import List


class Solution1:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        count = 0
        if len(A) < 3:
            return count
        start = 0
        end = start + 2
        hash_map = {}
        def find_uniq_diffs(i, j):
            for k in range(i+1, j+1):
                diff = A[k] - A[k-1]
                hash_map[diff] = k
            return hash_map

        while end < len(A):
            uniq_diff = find_uniq_diffs(start, end)
            if len(uniq_diff) == 1:
                count += 1
                if end == len(A)-1 and start+2 < end:
                    start += 1
                    end = start+2
                    hash_map = {}
                else:
                    end += 1
            else:
                if max(hash_map.values()) - start < 2:
                    start = max(hash_map.values())
                    end = start + 2
                    hash_map = {}
                else:
                    start += 1
                    end = start + 2
                    hash_map ={}
        return count


class Solution2:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        count = 0
        if len(A) < 3:
            return count
        for start in range(len(A)-2):
            d = A[start+1] - A[start]
            for end in range(start+2, len(A)):
                if A[end] - A[end-1] == d:
                    count += 1
                else:
                    break
        return count


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        """ Using Recursion"""
        sum = 0
        def slices(i):
            nonlocal sum
            if i < 2:
                return 0
            ap = 0
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                ap = 1 + slices(i-1)
                sum += ap
            else:
                slices(i-1)
            return ap

        import pdb;
        pdb.set_trace()
        slices(len(A)-1)
        return sum




A = [1, 2, 3, 4]
print(Solution().numberOfArithmeticSlices(A))
A = [1, 2, 3, 4, 6, 7, 8]

print(Solution().numberOfArithmeticSlices(A))

