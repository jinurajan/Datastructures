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


class Solution1(object):
    # Best for runtime with memoization
    def hammingWeight(self, n):
        if n <= 2:
            return mem_map[n]
        else:
            if n in mem_map:
                return mem_map[n]
            mem_map[n] = n % 2 + self.hammingWeight(n // 2)
        return mem_map[n]


class Solution2(object):
    # solution with while loop
    def hammingWeight(self, n):
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        else:
            no_of_bits = 0
            while n > 0:
                no_of_bits += n % 2
                n = n // 2
            return no_of_bits


class Solution3(object):
    # Solution with recursion
    def hammingWeight(self, n):
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        else:
            return n % 2 + self.hammingWeight(n // 2)


class Solution4(object):
    # solution with recursion without memoization
    def hammingWeight(self, n):
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        else:
            if n in mem_map:
                return mem_map[n]
            mem_map[n] = n % 2 + self.hammingWeight(n // 2)
        return mem_map[n]


if __name__ == "__main__":
    # print "number of bits in {} is {}".format(Solution().hammingWeight(0))
    # print Solution().hammingWeight(1)
    # print Solution().hammingWeight(2)
    # print Solution().hammingWeight(3)
    # print Solution().hammingWeight(4)
    # print Solution().hammingWeight(5)
    # print Solution().hammingWeight(6)
    # print Solution().hammingWeight(7)
    solution1 = Solution1()
    solution2 = Solution2()
    solution3 = Solution3()
    solution4 = Solution4()
    for i in range(16):
        print "number of bits in {} is {}".format(i, solution1.hammingWeight(i))
    print "************** Solution 2 *************"
    for i in range(16):
        print "number of bits in {} is {}".format(i, solution2.hammingWeight(i))
    # scale testing
    from time import time
    i = 12345678901234567
    current_time = time()
    print "number of bits in {} is {}".format(i, solution1.hammingWeight(i))
    print "time taken to compute number of bits in {} in solution 1 is:{}".format(
        i, float(time() - current_time))

    current_time = time()
    print "number of bits in {} is {}".format(i, solution2.hammingWeight(i))
    print "time taken to compute number of bits in {} in solution 2 is:{}".format(
        i, float(time() - current_time))

    current_time = time()
    print "number of bits in {} is {}".format(i, solution3.hammingWeight(i))
    print "time taken to compute number of bits in {} in solution 3 is:{}".format(
        i, float(time() - current_time))

    current_time = time()
    print "number of bits in {} is {}".format(i, solution4.hammingWeight(i))
    print "time taken to compute number of bits in {} in solution 4 is:{}".format(
        i, float(time() - current_time))
