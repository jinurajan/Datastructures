"""
Reverse String

Solution
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s)- 1)
        return s

    def reverse(self, s, first, last):
    	if first >= last:
    		return
    	s[first], s[last] = s[last], s[first]
    	self.reverse(s, first+1, last-1)



class Solution1(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        def reverse(s, first, last):
        	if first < last:
        		s[first], s[last] = s[last], s[first]
        		reverse(s, first+1, last-1)
        reverse(s, 0, len(s) - 1)
        return s

    	      
print Solution().reverseString(["h","e","l","l","o"])
print Solution().reverseString(["H","a","n","n","a","h"])

print Solution1().reverseString(["h","e","l","l","o"])
print Solution1().reverseString(["H","a","n","n","a","h"])