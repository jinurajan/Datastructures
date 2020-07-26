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

class SolutionwithLoop(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        j = len(s)-1
        for i in range(len(s)//2):
            s[i], s[j] = s[j], s[i]
            j -=1
        return s


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1:
            return s
        else:
            # more than 1 element in the array
            start_index = 0
            end_index = len(s) - 1
            while start_index < end_index:
                temp = s[start_index]
                s[start_index] = s[end_index]
                s[end_index] = temp
                end_index -= 1
                start_index += 1
        return s


def swap(s, i, j):
    s[i], s[j] = s[j], s[i]


def reverse_str(s, start_index, end_index):
    if start_index >= end_index:
        return s
    else:
        swap(s, start_index, end_index)
        s = reverse_str(s, start_index + 1, end_index - 1)
        return s


class SolutionRecursion(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1:
            return s
        else:
            return reverse_str(s, 0, len(s) - 1)


if __name__ == "__main__":
    array = ["h", "e", "l", "l", "o"]
    array1 = ["h", "e", "l", "l", "o"]
    array2 = ["h", "e", "l", "l", "o"]
    print Solution().reverseString(array)
    print SolutionRecursion().reverseString(array1)
    print SolutionwithLoop().reverseString(array2)

