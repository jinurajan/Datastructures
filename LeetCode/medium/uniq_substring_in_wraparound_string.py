"""
Unique Substrings in Wraparound String

Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.



'a' - > 1
'ab' -> 2
'abc' -> 6 (1+2+3)
'abcd' -> 10 (1+2+3+4)
"""
class Solution(object):
    mem = {0: 0, 1: 1}
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """ 
        def get_count(p):
            # maximum number of substrings of length n is
            # 1, 2 ---- n = n *(n +1)/2
            return p * (p+1) / 2

        def lcs(a):


        # char_set = set(p)
        # if len(p) == len(char_set):
        #     # no duplicate chars
        #     return get_count(len(char_set))
        # print get_count(len(char_set)) ,get_count(len(p)-len(char_set))
        # return get_count(len(char_set)) - get_count(len(p)-len(char_set))


# print Solution().findSubstringInWraproundString("zab") == 6
# print Solution().findSubstringInWraproundString("abcd") == 10
# print Solution().findSubstringInWraproundString("abcdef") == 21
print Solution().findSubstringInWraproundString("cac") == 2
print Solution().findSubstringInWraproundString("zaba") == 6

