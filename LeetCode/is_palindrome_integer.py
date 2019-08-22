class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == self.reverse_integer(x):
            return True
        return False

    def reverse_integer(self, x):
        
        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10
            reversed_num = reversed_num + x % 10
            x = x / 10
        return reversed_num


if __name__ == "__main__":
    print Solution().isPalindrome(121)
    print Solution().isPalindrome(123)
    print Solution().isPalindrome(100)
    print Solution().isPalindrome(101)
    print Solution().isPalindrome(111)
    print Solution().isPalindrome(-123)