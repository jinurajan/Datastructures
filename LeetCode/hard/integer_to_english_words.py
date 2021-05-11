"""
Convert a non-negative integer num to its English words representation.

Input: num = 123
Output: "One Hundred Twenty Three"

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

Constraints:

0 <= num <= 231 - 1

"""


class Solution:
    def numberToWords(self, num: int) -> str:
        def one(num):
            switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return switcher.get(num, '')

        def two_less_20(num):
            switcher = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switcher.get(num, '')

        def ten(num):
            switcher = {
                1: 'Ten',
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switcher.get(num, '')

        def two(num):
            if not num:
                return ''
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            else:
                tens, rest = divmod(num, 10)
                return ten(tens) + ' ' + one(rest) if rest else ten(tens)

        def three(num):
            hundreds, rest = divmod(num, 100)
            res = ''
            if hundreds:
                res += one(hundreds) + ' Hundred'
            if rest:
                if res:
                    res += ' '
                res += two(rest)
            return res

        billion, rest = divmod(num, pow(10, 9))
        million, rest = divmod(rest, pow(10, 6))
        thousand, rest = divmod(rest, 1000)

        if not num:
            return 'Zero'
        result = ''
        if billion:
            result += three(billion) + ' Billion'
        if million:
            if result:
                result += ' '
            result += three(million) + ' Million'
        if thousand:
            if result:
                result += ' '
            result += three(thousand) + ' Thousand'
        if rest:
            if result:
                result += ' '
            result += three(rest)
        return result



