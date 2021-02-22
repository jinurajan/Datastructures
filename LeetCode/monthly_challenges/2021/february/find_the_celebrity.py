"""
Find the Celebrity

Suppose you are at a party with n people (labeled from 0 to n - 1), and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her, but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
Example 2:


Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.
Constraints:

n == graph.length
n == graph[i].length
2 <= n <= 100
graph[i][j] is 0 or 1.
graph[i][i] == 1


Follow up: If the maximum number of allowed calls to the API knows is 3 * n, could you find a solution without exceeding the maximum number of calls?
"""


# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    matrix = [[1,0],[1,1]]
    return matrix[a][b]

class Solution1:
    def findCelebrity(self, n: int) -> int:

        def is_celebrity(i):
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j) or not knows(j, i):
                    return False
            return True
        for i in range(n):
            if is_celebrity(i):
                return i
        return -1



class Solution:
    def findCelebrity(self, n: int) -> int:
        def is_celebrity(i):
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j) or not knows(j, i):
                    return False
            return True
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
            if is_celebrity(candidate):
                return candidate
        return -1

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidates = set(range(n))
        mem = {}

        def if_knows(a, b):
            if (a, b) in mem:
                return mem[(a, b)]
            else:
                res = knows(a, b)
                mem[(a, b)] = res
                return res

        while len(candidates) > 1:
            it = iter(candidates)
            a = next(it)
            b = next(it)
            if if_knows(a, b):
                candidates.remove(a)
            else:
                candidates.remove(b)
        c = next(iter(candidates))
        for i in range(n):
            if c != i:
                if not if_knows(i, c) or if_knows(c, i):
                    return -1
        return c

from functools import lru_cache

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidates = set(range(n))

        @lru_cache(maxsize=None)
        def if_knows(a, b):
            return knows(a, b)

        while len(candidates) > 1:
            it = iter(candidates)
            a = next(it)
            b = next(it)
            if if_knows(a, b):
                candidates.remove(a)
            else:
                candidates.remove(b)
        c = next(iter(candidates))
        for i in range(n):
            if c != i:
                if not if_knows(i, c) or if_knows(c, i):
                    return -1
        return c




print(Solution().findCelebrity(2))


