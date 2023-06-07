"""
Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.


"""


from functools import lru_cache


class Solution:
    """
    1. reverse byte by bytes ie 8 bits at a time

    byte1, byte2, byte3, byte4 -> byte4, byte3, byte2, byte1

    oxff -> 11111111 

    f in hexadecimal is 1111

    0x0202020202 -> 1000000010000000100000001000000010 -> 64 bytes
    0x010884422010 -> 10000100010000100010000100010000000010000
    """
    @lru_cache(maxsize=256)
    def reversebytes(self, byte):
        return (byte * 0x0202020202 & 0x010884422010) % 1023

    def reverseBits(self, n: int) -> int:
        result = 0
        power = 24
        while n:
            result += self.reversebytes(n & 0xff)  << power 
            n >>= 8
            power -= 8
        return result
    

class Solution:
    def reverseBits(self, n: int) -> int:
        # http://graphics.stanford.edu/~seander/bithacks.html#ReverseByteWith64BitsDiv
        # bit by bit
        """
        1. start with zero
        2. n shift to right by power to get the right most bit and now move it to left by shifting to left
        3. reduce the power by 1
        4. reset n by right shifting 1
        """
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n >>= 1
            power -= 1
        return ret


class Solution:
    
    def reverseBits(self, n):
        """
        for 8 bit binary number abcdefgh, the process is as follow:
        abcdefgh -> efghabcd -> ghefcdab -> hgfedcba

        0xff00ff00 - 11111111000000001111111100000000
        0x00ff00ff - 00000000111111110000000011111111
        0xf0f0f0f0 - 11110000111100001111000011110000
        0x0f0f0f0f - 00001111000011110000111100001111
        0xcccccccc - 11001100110011001100110011001100
        0x33333333 - 00110011001100110011001100110011
        0xaaaaaaaa - 10101010101010101010101010101010
        0x55555555-  01010101010101010101010101010101
        """
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n