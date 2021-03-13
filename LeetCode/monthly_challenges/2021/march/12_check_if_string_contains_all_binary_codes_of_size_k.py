"""
Check If a String Contains All Binary Codes of Size K

Given a binary string s and an integer k.

Return True if every binary code of length k is a substring of s. Otherwise, return False.

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.
Example 2:

Input: s = "00110", k = 2
Output: true
Example 3:

Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.
Example 4:

Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and doesn't exist in the array.
Example 5:

Input: s = "0000000001011100", k = 4
Output: false
"""

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        no_of_codes = 1 << k
        got = [False] * no_of_codes
        all_one = no_of_codes -1
        hash_val = 0
        for i in range(len(s)):
            print(hash_val)
            hash_val = ((hash_val << 1) & all_one) | (int(s[i]))
            if i >= k-1 and got[hash_val] is False:
                got[hash_val] = True
                no_of_codes -= 1
                if no_of_codes == 0:
                    return True
        return False


class Solution1:
    def hasAllCodes(self, s: str, k: int) -> bool:
        no_of_codes = 1 << k
        code_set = set()
        for i in range(k, len(s) + 1):
            tmp = s[i - k:i]
            code_set.add(tmp)

        return len(code_set) == no_of_codes


print(Solution().hasAllCodes("00110110", 2))