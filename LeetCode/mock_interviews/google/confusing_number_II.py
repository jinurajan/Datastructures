"""
Confusing Number II
We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.

A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.)

Given a positive integer n, return the number of confusing numbers between 1 and n inclusive.



Example 1:

Input: n = 20
Output: 6
Explanation:
The confusing numbers are [6,9,10,16,18,19].
6 converts to 9.
9 converts to 6.
10 converts to 01 which is just 1.
16 converts to 91.
18 converts to 81.
19 converts to 61.
Example 2:

Input: n = 100
Output: 19
Explanation:
The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].

"""


class Solution:
    def confusingNumberII(self, n: int) -> int:
        confusing_no = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        result = []
        nums = list(confusing_no.keys())
        count = 0

        def flippable(num):
            start, end = 0, len(num) - 1
            while start <= end:
                if confusing_no[num[start]] == num[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True

        def dfs(num):
            nonlocal count
            if int(num) > n:
                return
            if not flippable(num):
                count += 1
            for next_digit in nums:
                next_num = num + next_digit
                dfs(next_num)

        for num in nums[1:]:
            dfs(num)

        return count





