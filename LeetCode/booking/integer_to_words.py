"""
Integer to English Words

Convert a non-negative integer num to its English words representation.
"""


class Solution:
    def numberToWords(self, num: int) -> str:

        def one(num):
            switch = {
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
            return switch[num]
        
        def two_less_20(num):
            switch = {
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
            return switch[num]
        
        def ten(num):
            switch = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switch[num]

        def two(num):
            if not num:
                return ''
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            else:
                tens, remainder = divmod(num, 10)
                return ten(tens) + ' ' + one(remainder) if remainder else ten(tens)
        
        def three(num):
            hundreds, rest = divmod(num, 100)
            result = ''
            if hundreds:
                result += one(hundreds) + " Hundred"
            if rest:
                result += " " if result else ""
                result += two(rest)
            return result


        if not num:
            return "Zero"

        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000

        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = (num - billion * 1000000000 - million * 1000000 - thousand*1000)

        result = ''
        if billion:
            result = three(billion) + " Billion"
        if million:
            result += " " if result else ""
            result += three(million) + ' Million'
        
        if thousand:
            result += " " if result else ""
            result += three(thousand) + ' Thousand'
        
        if rest:
            result += " " if result else ""
            result += three(rest)
        
        return result


print(Solution().numberToWords(1234567890))
print(Solution().numberToWords(99))
print(Solution().numberToWords(1))
print(Solution().numberToWords(0))
print(Solution().numberToWords(19))
print(Solution().numberToWords(20))
print(Solution().numberToWords(120))