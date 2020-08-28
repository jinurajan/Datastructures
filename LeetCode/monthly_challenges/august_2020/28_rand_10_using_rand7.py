"""

Implement Rand10() Using Rand7()


Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().

Example 1:

Input: 1
Output: [7]
Example 2:

Input: 2
Output: [8,4]
Example 3:

Input: 3
Output: [8,1,10]


Note:

rand7 is predefined.
Each testcase has one argument: n, the number of times that rand10 is called.

Follow up:

What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?


Solution:
1. can we generate rand10 with one rand7 calls ? no. lets use 2 then
2. generate a and b both from rand7. overall distribution is then 49 (which is from 1-49). we want from 0-9
c = (a-1) * 7 + b-1 means (a-1 means 0 to 6 - 7 times and b-1 means (0-6 again)).so total 48 distributions (0 - 48)
3. take these into groups : [0:9], [10:19], [20:29], [30:39], [40:48] (except 5th we have all 10 equal distribution.)
4. reject sample if value falls into [40:48] category meaning start over again
5. otherwise use % 10 + 1 (because we want from 1-9 not from 0-8)

"""
import random


def rand7():
    return random.randint(1, 7)


def rand3():
    return random.randint(1, 3)


class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        c = (rand7() - 1) * 7 + rand7()
        if c >= 40:
            return self.rand10()
        else:
            return (c % 10) + 1


class Solution1(object):
    def rand10(self):
        """
        :rtype: int
        """
        random = 41
        while random > 40:
            random = 7 * (rand7() - 1) + (rand7())
        return (random % 10) + 1



# rand5 using rand3

class Solution2(object):
    def rand5(self):
        """
        :rtype: int
        """
        c = (rand3() - 1) * 3 + rand3() - 1
        if c >= 6:
            return self.rand5()
        else:
            return (c % 5) + 1

# print Solution().rand10()
# print Solution1().rand10()
print Solution2().rand5()
# print Solution().rand10()
# print Solution().rand10()
# print Solution().rand10()
# print Solution().rand10()
# print Solution().rand10()
# print Solution().rand10()
# print Solution().rand10()
# print Solution().rand10()