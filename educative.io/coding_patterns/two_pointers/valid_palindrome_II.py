"""
Write a function that takes a string as input and checks whether it can be a valid palindrome by removing at most one character from it.

Constraints:

1
1
 
≤
≤
 string.length 
≤
1
0
5
≤10 
5
 

The string only consists of English letters
"""



def is_palindrome(s):
    # Write your code here
    # Tip: You may use the code template provided
    # in the two_pointers.py file
    start = 0
    end = len(s)-1


    def palindrome_check(start, end, s):
        while start < end and start < len(s) and end < len(s):
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            if palindrome_check(start+1, end, s) or palindrome_check(start, end-1, s):
                return True
            return False
    return False
    
from collections import Counter
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                tmp1 = s[:l] + s[l+1:]
                tmp2 = s[:r] + s[r+1:]
                return tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]
        return True




  
print(is_palindrome("madame"))
print(is_palindrome("dead"))
print(is_palindrome("abca"))

print(is_palindrome("tebbem"))
print(is_palindrome("eeccccbebaeeabebccceea"))