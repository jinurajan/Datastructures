"""
First Bad Version

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
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid
        if not isBadVersion(l):
            return r
        else:
            return l

class Solution1:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        def binary_search(l, r, min_version):
            if l <= r:
                mid = (l + r) // 2
                if isBadVersion(mid+1):
                    min_version[0] = min(min_version[0], mid+1)
                    return binary_search(l, mid-1, min_version)
                else:
                    return binary_search(mid + 1, r, min_version)
        min_version = [n+1]
        binary_search(0, n-1, min_version)
        return min_version[0]


class Solution2:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = -1
        start = n
        while start >= 1:
            while not isBadVersion(x+start):
                x += start
            start //= 2
        return x + 1

