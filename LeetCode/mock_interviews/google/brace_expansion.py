"""
Brace Expansion

You are given a string s representing a list of words. Each letter in the word has one or more options.

If there is one option, the letter is represented as is.
If there is more than one option, then curly braces delimit the options. For example, "{a,b,c}" represents options ["a", "b", "c"].
For example, if s = "a{b,c}", the first character is always 'a', but the second character can be 'b' or 'c'. The original list is ["ab", "ac"].

Return all words that can be formed in this manner, sorted in lexicographical order.



Example 1:

Input: s = "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:

Input: s = "abcd"
Output: ["abcd"]


Constraints:

1 <= s.length <= 50
s consists of curly brackets '{}', commas ',', and lowercase English letters.
s is guaranteed to be a valid input.
There are no nested curly brackets.
All characters inside a pair of consecutive opening and ending curly brackets are different.

"""


class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        self.result = []

        def helper(s, word):
            if not s:
                self.result.append(word)
            else:
                if s[0] == '{':
                    i = s.find("}")
                    for ch in s[1:i].split(","):
                        helper(s[i + 1:], word + ch)
                else:
                    helper(s[1:], word + s[0])

        helper(S, "")
        self.result.sort()
        return self.result


class Solution:
    def expand(self, s: str) -> List[str]:
        arr = []
        p = []
        start = False
        for char in s:
            if char == '{':
                start = True
                continue
            if char == "}":
                start = False
                arr.append(sorted(p))
                p = []
                continue
            if start:
                if char != ',':
                    p.append(char)
                continue
            else:
                arr.append(char)
        result = []
        n = len(arr)

        def dfs(index, paths):
            nonlocal result
            if index == n:
                result.append("".join(paths[:]))
                return
            if type(arr[index] == list):
                for each in arr[index]:
                    paths.append(each)
                    dfs(index + 1, paths)
                    paths.pop()
            else:
                paths.append(arr[index])
                dfs(index + 1, paths)

        dfs(0, [])
        return result





