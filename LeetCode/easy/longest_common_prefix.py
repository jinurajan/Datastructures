"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        min_length = len(strs[0])
        result = ""
        for i in range(1, len(strs)):
            if len(strs[i]) < min_length:
                min_length = len(strs[i])
        # found the minimum length value
        for i in range(min_length):
            current = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != current:
                    return result
            result += current
        return result


if __name__ == "__main__":
    print Solution().longestCommonPrefix(["flower", "flow", "flight"])
    print Solution().longestCommonPrefix(["dog", "racecar", "car"])
    print Solution().longestCommonPrefix(["a"])
    print Solution().longestCommonPrefix(["c", "c"])