"""
Count Number of Teams
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4


Constraints:

n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 105
All the integers in rating are unique.

"""
from typing import List
import bisect



class Solution:
    def numTeams(self, rating: List[int]) -> int:
        leftPos = []

        L = []

        for r in rating:
            leftPos.append(bisect.bisect(L,r))
            bisect.insort(L,r)

        rightPos = [-1]*len(rating)

        R = []

        for idx in range(len(rating)-1,-1,-1):
            r = rating[idx]
            rightPos[idx] = (bisect.bisect(R,r))
            bisect.insort(R,r)


        ans = 0

        for idx in range(1,len(rating)-1):
            ans += leftPos[idx]*(len(rating)-1-idx-rightPos[idx])
            ans += rightPos[idx]*(idx-leftPos[idx])

        return ans



class Solution1:
    def numTeams(self, rating: List[int]) -> int:

        n = len(rating)
        dp_inc = [[0 for _ in range(3)] for _ in range(n)]
        dp_dec = [[0 for _ in range(3)] for _ in range(n)]

        for i in range(n):
            dp_inc[i][0] = 1
            dp_dec[i][0] = 1

        for i in range(1, n):
            for j in range(i):
                for k in range(1, 3):
                    if rating[j] < rating[i]:
                        dp_inc[i][k] += dp_inc[j][k-1]
                    else:
                        dp_dec[i][k] += dp_dec[j][k-1]

        total = 0
        for i in range(n):
            total += dp_inc[i][2]
            total += dp_dec[i][2]

        return total


rating = [2,5,3,4,1]
print(Solution().numTeams(rating))