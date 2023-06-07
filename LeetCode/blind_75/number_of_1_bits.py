"""
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        # shift the n right side until it becomes zero
        count = 0
        while n:
            if n & 1:
                count += 1
            n >>= 1
        return count
    
class Solution:
    def hammingWeight(self, n: int) -> int:
        # shift the mask ie 1 bit set value to left and do and with the bit 
        count = 0
        mask = 1
        for i in range(32):
            if n & mask:
                count += 1
            mask <<= 1
        return count

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= (n-1)
        return count