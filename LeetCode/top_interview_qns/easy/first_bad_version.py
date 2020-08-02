"""
First Bad Version

Solution
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.

"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


def isBadVersion(val):
    print 'isBadVersion', val
    if val >= 60:
        return True
    else:
        return False


class Solution1(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
        l = 0
        r = n
        first = -1
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                first = m
                r = m - 1
            else:
                l = m + 1
        return first


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
        return self.check_first_bad(n, 1, n)

    def check_first_bad(self, n, lower, upper):
        if upper - lower <= 1:
            # near by values close proximity
            # return lower
            if isBadVersion(lower):
                return lower
            else:
                return upper
        middle = (lower + upper) // 2
        if isBadVersion(middle):
            # lying on the left
            upper = middle
        else:
            lower = middle
        return self.check_first_bad(n, lower, upper)


if __name__ == "__main__":
    # print Solution().firstBadVersion(2)
    # print Solution().firstBadVersion(100)
    print Solution1().firstBadVersion(100)
    # print Solution().firstBadVersion(10)
    # print Solution().firstBadVersion(6)
