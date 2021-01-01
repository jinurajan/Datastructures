"""
 Excel Sheet Column Number
 Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = 0
        no = 0
        i = len(s) - 1
        while i >= 0:
            value += (ord(s[i]) - ord('A')+1)* pow(26, no)
            no += 1
            i -= 1
        return value


if __name__ == "__main__":
    print Solution().titleToNumber('A')
    print Solution().titleToNumber('AA')
    print Solution().titleToNumber('AB')
    print Solution().titleToNumber('AC')
    print Solution().titleToNumber('ZY')
    print Solution().titleToNumber('Z')
    print Solution().titleToNumber('ZA')
