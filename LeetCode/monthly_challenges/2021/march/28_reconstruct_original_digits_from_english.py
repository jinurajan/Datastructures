"""
Reconstruct Original Digits from English
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
"""
from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        out = {}
        out["0"] = count["z"]
        out["2"] = count["w"]
        out["4"] = count["u"]
        out["6"] = count["x"]
        out["8"] = count["g"]
        out["3"] = count["h"] - out["8"]
        out["5"] = count["f"] - out["4"]
        out["7"] = count["s"] - out["6"]
        out["9"] = count["i"] - out["5"] - out["6"] - out["8"]
        out["1"] = count["n"] - out["7"] - 2 * out["9"]
        output = [key * out[key] for key in sorted(out.keys())]
        return "".join(output)


class Solution1:
    def originalDigits(self, s: str) -> str:
        result = ""
        counter = Counter(s)
        digit_map = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
                     "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

        def convert_to_digit():
            if not counter:
                return
            res = ""
            for digit, val in digit_map.items():
                digi_set = set(digit)
                if digi_set.intersection(set(s)) != digi_set:
                    continue
                for d in digit:
                    if d not in counter:
                        return res
                    counter[d] -= 1
                    if counter[d] == 0:
                        del counter[d]
                res += val
            return res

        while counter:
            digit = convert_to_digit()
            if not digit:
                break
            result += digit
        return result




s = "zerozero"
print(Solution().originalDigits(s))
s = "owoztneoer"
print(Solution().originalDigits(s))
s = "fviefurofviefuro"
print(Solution().originalDigits(s))

