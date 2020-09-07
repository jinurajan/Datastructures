"""
1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K (medium)
Given the number k, return the minimum number of Fibonacci numbers whose sum is equal to k, whether a Fibonacci number could be used multiple times.

The Fibonacci numbers are defined as:

F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 , for n > 2.
It is guaranteed that for the given constraints we can always find such fibonacci numbers that sum k.

Example 1:

Input: k = 7
Output: 2
Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ...
For k = 7 we can use 2 + 5 = 7.
Example 2:

Input: k = 10
Output: 2
Explanation: For k = 10 we can use 2 + 8 = 10.
Example 3:

Input: k = 19
Output: 3
Explanation: For k = 19 we can use 1 + 5 + 13 = 19.


Constraints:

1 <= k <= 10^9

"""
from sys import maxint

fib_values = {}


def get_fib(k):
    fib_values[0] = 1
    fib_values[1] = 1
    s = 0
    for i in range(2, k + 1):
        val = fib_values[i - 1] + fib_values[i - 2]
        s += val
        if val >= k or s >= k:
            break
        fib_values[i] = val
    return fib_values


class Solution1(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        # T[i] = min(T[i], 1+ T[i-fibs[j]]) if i >=fibs[j]
        fibs = sorted(get_fib(k).values())[1:]# fibs here
        print fibs
        solution = [maxint] * (k + 1)
        solution[0] = 0
        for j in xrange(len(fibs)):
            for i in xrange(k + 1):
                if i >= fibs[j]:
                    solution[i] = min(solution[i], 1 + solution[i - fibs[j]])
        return solution[k]


class Solution1(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        fibs = [1,1]
        if k == 1:
            return 1
        counter = 0
        while True:
            fibs.append(fibs[-1] + fibs[-2])
            res = k - fibs[-1]
            if res < 1:
                if res == 1:
                    return 1
                break

        for f_n in reversed(fibs):
            res = k - f_n
            if res < 0:
                continue
            if res == 0:
                return counter + 1
            k = res
            counter += 1











# print Solution().findMinFibonacciNumbers(10) == 2
# print Solution().findMinFibonacciNumbers(7) == 2
# print Solution().findMinFibonacciNumbers(19) == 3
print Solution().findMinFibonacciNumbers(9083494)

