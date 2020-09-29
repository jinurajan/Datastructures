"""
Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

-1: The number I picked is lower than your guess (i.e. pick > num).
1: The number I picked is higher than your guess (i.e. pick < num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.

 

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
Example 4:

Input: n = 2, pick = 2
Output: 2
 

Constraints:

1 <= n <= 231 - 1
1 <= pick <= n
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    if num > X:
        return -1
    if num < X:
        return 1
    return 0

class Solution2(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def binary_guess(l, r):
            if l <= r:
                mid = (l + r)/ 2
                guess_val = guess(mid)
                if guess_val== 0:
                    return mid
                elif guess_val == -1:
                    return binary_guess(l, mid - 1)
                else:
                    return binary_guess(mid + 1, r)

        return binary_guess(0, n)



class Solution1(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n
        while l <=r:
            mid = (l + r) / 2
            guess_val = guess(mid)
            if guess_val== 0:
                return mid
            elif guess_val == -1:
                r = mid - 1
            else:
                l = mid + 1


X = 6
print Solution().guessNumber(10)
print Solution1().guessNumber(10)
X = 2
print Solution().guessNumber(15)
print Solution1().guessNumber(10)








