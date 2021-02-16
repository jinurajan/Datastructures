"""
First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Input: n = 1, bad = 1
Output: 1

Constraints:

1 <= bad <= n <= 231 - 1

"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    print("called")
    if version >= 2:
        return True
    return False

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first_bad_version = n
        def binary_search(first, last):
            nonlocal first_bad_version
            if first < last:
                mid = (first + last ) // 2
                if isBadVersion(mid):
                    first_bad_version = min(first_bad_version, mid)
                    last = mid
                else:
                    first = mid + 1
                binary_search(first, last)
        binary_search(0, n)
        return first_bad_version


print(Solution().firstBadVersion(6))