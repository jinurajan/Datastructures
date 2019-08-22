"""

"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        i = len(s) - 1
        value = Roman_numerals[s[i]]
        i -= 1
        while i >= 0:
            if(Roman_numerals[s[i]] >= Roman_numerals[s[i+1]]):
                value += Roman_numerals[s[i]]
            else:
                value -= Roman_numerals[s[i]]

            i -= 1
        return value


if __name__ == "__main__":
    # print Solution().romanToInt("III")
    # print Solution().romanToInt("IV")
    # print Solution().romanToInt("LVIII")
    print Solution().romanToInt("MCMXCIV")