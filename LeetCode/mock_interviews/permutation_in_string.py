"""
Permutation in String
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_sum = s2_sum = 0
        for symbol in s1:
            s1_sum += hash(symbol)
        for i in range(len(s1)):
            s2_sum += hash(s2[i])
        if s2_sum == s1_sum:
            return True
        first_index = 0
        for i in range(len(s1), len(s2)):
            s2_sum += hash(s2[i])
            s2_sum -= hash(s2[first_index])
            if s2_sum == s1_sum:
                return True
            first_index += 1
        return False


class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        map_s1 = [0 for i in range(26)]
        for char in s1:
            map_s1[ord(char)-ord('a')] += 1
        for i in range(len(s2)-len(s1)+1):
            map_s2 = [0 for i in range(26)]
            for j in range(len(s1)):
                print(i, j)
                map_s2[ord(s2[i+j])-ord('a')] += 1
            if map_s1 == map_s2:
                return True
        return False

if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    Solution1().checkInclusion(s1, s2)
    s2 = "eidboaoo"
    Solution1().checkInclusion(s1, s2)

