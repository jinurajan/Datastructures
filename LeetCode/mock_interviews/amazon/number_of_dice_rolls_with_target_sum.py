"""
Number of Dice Rolls With Target Sum

You have d dice and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 109 + 7 to roll the dice so the sum of the face-up numbers equals target.

Input: d = 1, f = 6, target = 3
Output: 1
Explanation:
You throw one die with 6 faces.  There is only one way to get a sum of 3.

Input: d = 2, f = 6, target = 7
Output: 6
Explanation:
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Input: d = 2, f = 5, target = 10
Output: 1
Explanation:
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.

Input: d = 1, f = 2, target = 3
Output: 0
Explanation:
You throw one die with 2 faces.  There is no way to get a sum of 3.

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation:
The answer must be returned modulo 10^9 + 7.

Constraints:

1 <= d, f <= 30
1 <= target <= 1000
"""


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        matrix = [[0] * target for i in range(d)]

        for col in range(f):
            if col > len(matrix[0]) - 1:
                break
            matrix[0][col] = 1

        for index in range(1, d):
            boundary = index if index < f else f
            previous_sum = sum(matrix[index - 1][index - boundary:index])
            running_sum = previous_sum

            for j in range(index, target):
                matrix[index][j] = running_sum
                if j >= f:
                    running_sum -= matrix[index - 1][j - f]
                running_sum += matrix[index - 1][j]

        count = matrix[d - 1][target - 1]

        if count < 0:
            count = 0
        return count % (1000000007)


class Solution1:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 1000000000+7
        dp =[[0 for i in range(target+1)] for j in range(d)]
        for i in range(d):
            for j in range(target+1):
                if i == 0:
                    dp[i][j] = 1 if j>=1 and j<=f else 0
                else:
                    for l in range(1,f+1):
                        if j-l>0:
                            dp[i][j] += dp[i-1][j-l]
                            dp[i][j] %= mod
        return dp [d-1][target] % mod


