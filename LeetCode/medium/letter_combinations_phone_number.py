"""
17. Letter Combinations of a Phone Number (medium)
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
class Solution(object):
    CHAR_HASH = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
    }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        import pdb; pdb.set_trace()
        self.find_combinations(digits, 0, res, "")
        return res

    def find_combinations(self, digits, curr_index, res, curr_str):
        if curr_index == len(digits):
            # length is now equal to index
            if curr_str:
                res.append(curr_str)
            return
        curr_digit = digits[curr_index]
        values = self.CHAR_HASH.get(curr_digit, [])
        for i in range(len(values)):
            curr_str += values[i]
            self.find_combinations(digits, curr_index+1, res, curr_str)
            curr_str = "".join(curr_str[:-1])


# print Solution().letterCombinations("23")
print Solution().letterCombinations("234")
# print Solution().letterCombinations("2345")