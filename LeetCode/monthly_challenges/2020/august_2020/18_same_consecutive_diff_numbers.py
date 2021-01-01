"""
Numbers With Same Consecutive Differences

Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Note:

1 <= N <= 9
0 <= K <= 9
"""


class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            # return all digits with length 1
            return [i for i in range(10)]
        else:
            results = []
            for num in range(1, 10):
                self.dfs(N - 1, num, K, results)
        return results

    def dfs(self, N, num, K, results):
        if N == 0:
            results.append(int(num))
            return
        next_digits = []
        tail_digit = num % 10
        next_digits.append(tail_digit + K)
        if K != 0:
            next_digits.append(tail_digit - K)
        for next_digit in next_digits:
            if next_digit >= 0 and next_digit < 10:
                new_num = (num * 10) + next_digit
                self.dfs(N - 1, new_num, K, results)


print Solution().numsSameConsecDiff(3, 7) == [181,292,707,818,929]
print Solution().numsSameConsecDiff(2, 1) == [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
print Solution().numsSameConsecDiff(4, 6) == [1717, 2828, 3939, 6060, 7171, 8282, 9393]