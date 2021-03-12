"""
Confusing Number
Given a number N, return true if and only if it is a confusing number, which satisfies the following condition:

We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid. A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.



Example 1:



Input: 6
Output: true
Explanation:
We get 9 after rotating 6, 9 is a valid number and 9!=6.
Example 2:



Input: 89
Output: true
Explanation:
We get 68 after rotating 89, 86 is a valid number and 86!=89.
Example 3:



Input: 11
Output: false
Explanation:
We get 11 after rotating 11, 11 is a valid number but the value remains the same, thus 11 is not a confusing number.
Example 4:



Input: 25
Output: false
Explanation:
We get an invalid number after rotating 25.


Note:

0 <= N <= 10^9
After the rotation we can ignore leading zeros, for example if after rotation we have 0008 then this number is considered as just 8.

"""
from math import log10


class Solution:
    def confusingNumber(self, N: int) -> bool:
        if not N:
            return False
        compliments = {1: 1, 0: 0, 9: 6, 6: 9, 8: 8}
        n = int(log10(N)) + 1
        r_pos = pow(10, n - 1)
        rotated_no = 0
        input_val = N
        while N > 0:
            N, r = divmod(N, 10)
            if r not in compliments:
                return False
            rotated_no += compliments.get(r) * r_pos
            r_pos /= 10
        return input_val != rotated_no


class Solution:
    def confusingNumber(self, N: int) -> bool:
        d = {'0': '0',
             '1': '1',
             '2': 'x',
             '3': 'x',
             '4': 'x',
             '5': 'x',
             '6': '9',
             '7': 'x',
             '8': '8',
             '9': '6'}

        txt = [d[i] for i in str(N)[::-1]]
        try:
            x = int(''.join(txt))
        except:
            return False
        if x == N:
            return False
        return True