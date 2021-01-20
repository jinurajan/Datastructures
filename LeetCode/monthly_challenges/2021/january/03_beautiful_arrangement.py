"""
Beautiful Arrangement

Suppose you have n integers from 1 to n. We define a beautiful arrangement as an array that is constructed by these n numbers successfully if one of the following is true for the ith position (1 <= i <= n) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Given an integer n, return the number of the beautiful arrangements that you can construct.

Input: n = 2
Output: 2
Explanation:
The first beautiful arrangement is [1, 2]:
Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
The second beautiful arrangement is [2, 1]:
Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.


Input: n = 1
Output: 1

Constraints:

1 <= n <= 15

"""
from itertools import permutations


class Solution2:
    def countArrangement(self, n: int) -> int:
        if n <= 2:
            return n

        def get_count(perm):
            for i in range(len(perm)):
                if not perm[i] % (i+1) or not (i+1) % perm[i]:
                    continue
                else:
                    return 0
            return 1
        count = 0
        for perm in permutations(range(1, n+1)):
            count += get_count(perm)
        return count

class Solution1:
    def countArrangement(self, n: int) -> int:
        if n <= 2:
            return n
        visited = [0 for i in range(n+1)]
        count = [0]
        def calculate(n, pos, visited):
            if pos > n:
                count[0] += 1
            for i in range(1, n+1):
                if not visited[i] and (not pos % i or not i % pos):
                    visited[i] = 1
                    calculate(n, pos + 1, visited)
                    visited[i] = 0

        calculate(n, 1, visited)
        return count[0]


cache = {}
class Solution:
    def countArrangement(self, n: int) -> int:
        def helper(i, perm):
            if i == 1:
                return 1
            if (i, perm) in cache:
                return  cache[(i, perm)]
            total = 0
            for j in range(len(perm)):
                if perm[j] % i == 0 or i % perm[j] == 0:
                    total += helper(i-1, perm[:j] + perm[j+1:])
            cache[(i, perm)] = total
            return total
        return  helper(n, tuple(range(1, n+1)))



print(Solution().countArrangement(1))
print(Solution().countArrangement(2))
print(Solution().countArrangement(3))
print(Solution().countArrangement(4))
print(Solution().countArrangement(5))