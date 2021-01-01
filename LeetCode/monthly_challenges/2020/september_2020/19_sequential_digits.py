"""
Sequential Digits 

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 
Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
"""

class Solution1(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        Using iteration
        """
        result = []
        for start in range(1, 10):
            x = start
            for y in range(start+1, 10):
                x = x * 10
                x += y

                if x >= low and x <=high:
                    result.append(x)
                if x > high:
                    break
        return sorted(result)





class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        def helper(low, high, result, start_digit, len_digit):
            if start_digit + len_digit > 10:
                start_digit = 1
                len_digit += 1
            new_digit = int("".join([str(i) for i in range(start_digit, start_digit+len_digit)]))
            if new_digit > high:
                return result
            if new_digit >= low and new_digit <= high:
                result.append(new_digit)
            helper(low, high, result, start_digit+1, len_digit)

        result = []
        l = len(str(low))
        start_digit = int(str(low)[0])
        helper(low, high, result, start_digit, len(str(low)))
        return result



# print Solution().sequentialDigits(100, 300)
# print Solution().sequentialDigits(1000, 13000)
# print Solution().sequentialDigits(2000, 13000)
# print Solution().sequentialDigits(234, 2314)
# print Solution().sequentialDigits(234, 2345)


print Solution1().sequentialDigits(100, 300)
print Solution1().sequentialDigits(1000, 13000)
print Solution1().sequentialDigits(2000, 13000)
print Solution1().sequentialDigits(234, 2314)
print Solution1().sequentialDigits(234, 2345)
