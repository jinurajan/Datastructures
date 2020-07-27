"""
Number of 1 Bits

Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

 

Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.
 

Follow up:

If this function is called many times, how would you optimize it?
"""
mem_map = {0: 0, 1: 1, 2: 1}


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if 0 <= n <= 2:
            return mem_map[n]
        else:
            # if n // 2 not in mem_map:
            #     mem_map[n // 2] = self.hammingWeight(n // 2)
            # if n - (n * (n // 2)) not in mem_map:
            #     mem_map[n - (n * (n // 2))] = self.hammingWeight(n - (n * (n // 2)))
            # mem_map[n] = mem_map[n // 2] + mem_map[n - (n * (n // 2))]
            # return mem_map[n]



if __name__ == "__main__":
    print Solution().hammingWeight(0)
    print Solution().hammingWeight(1)
    print Solution().hammingWeight(2)
    print Solution().hammingWeight(3)
    print Solution().hammingWeight(4)
    print Solution().hammingWeight(5)
    print Solution().hammingWeight(6)
    print Solution().hammingWeight(7)

