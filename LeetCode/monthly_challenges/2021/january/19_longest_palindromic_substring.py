"""
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.


Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""

class Solution:
    MEM = {}
    def longestPalindrome(self, s: str) -> str:
        for sub_len in range(len(s), 0, -1):
            for j in range(len(s)):
                substr = s[j:j + sub_len]
                if len(substr) != sub_len:
                    continue
                if not substr in self.MEM:
                    if self.is_palindrome(substr, 0, len(substr)-1):
                        return substr
                    else:
                        self.MEM[substr] = False

    def is_palindrome(self, s: str, start: int, end:int) -> bool:
        if len(s) == 1:
            return True
        if abs(start-end) == 1 and s[start] == s[end]:
            return  True
        if start == end:
            return True
        if start > end:
            return False
        if s[start] != s[end]:
            return False
        return self.is_palindrome(s, start+1, end-1)

print(Solution().longestPalindrome("anugnxshgonmqydttcvmtsoaprxnhpmpovdolbidqiyqubirkvhwppcdyeouvgedccipsvnobrccbndzjdbgxkzdbcjsjjovnhpnbkurxqfupiprpbiwqdnwaqvjbqoaqzkqgdxkfczdkznqxvupdmnyiidqpnbvgjraszbvvztpapxmomnghfaywkzlrupvjpcvascgvstqmvuveiiixjmdofdwyvhgkydrnfuojhzulhobyhtsxmcovwmamjwljioevhafdlpjpmqstguqhrhvsdvinphejfbdvrvabthpyyphyqharjvzriosrdnwmaxtgriivdqlmugtagvsoylqfwhjpmjxcysfujdvcqovxabjdbvyvembfpahvyoybdhweikcgnzrdqlzusgoobysfmlzifwjzlazuepimhbgkrfimmemhayxeqxynewcnynmgyjcwrpqnayvxoebgyjusppfpsfeonfwnbsdonucaipoafavmlrrlplnnbsaghbawooabsjndqnvruuwvllpvvhuepmqtprgktnwxmflmmbifbbsfthbeafseqrgwnwjxkkcqgbucwusjdipxuekanzwimuizqynaxrvicyzjhulqjshtsqswehnozehmbsdmacciflcgsrlyhjukpvosptmsjfteoimtewkrivdllqiotvtrubgkfcacvgqzxjmhmmqlikrtfrurltgtcreafcgisjpvasiwmhcofqkcteudgjoqqmtucnwcocsoiqtfuoazxdayricnmwcg"))
print(Solution().longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(Solution().longestPalindrome("eabcb"))
print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbbbd"))
print(Solution().longestPalindrome("a"))
print(Solution().longestPalindrome("ac"))


