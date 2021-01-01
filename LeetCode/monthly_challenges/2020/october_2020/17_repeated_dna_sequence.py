"""
Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

0 <= s.length <= 105
s[i] is 'A', 'C', 'G', or 'T'.
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if not s or len(s) < 10:
            return []
        hash_set = {}
        res = []
        for i in range(len(s)-9):
            substring = s[i:i+10]
            hash_set[substring] = hash_set.get(substring, 0) + 1
            if hash_set[substring] == 2:
                res.append(substring)
        return res
        