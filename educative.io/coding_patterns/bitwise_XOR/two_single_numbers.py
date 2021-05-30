"""
In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once. Find the two numbers that appear only once.

Example 1:

Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
Output: [4, 6]
Example 2:

Input: [2, 1, 3, 2]
Output: [1, 3]

1. do xor of all numbers you will get both numbers xored value
2. find the rightmost bit which is set
3. divide the set into to in such a way that that bit is set do xor of each group
"""


def find_single_numbers(nums):
    both_xor = 0
    for num in nums:
        both_xor ^= num
    # find bit which is one
    # get the rightmost bit that is '1'
    rightmost_set_bit = 1
    while (rightmost_set_bit & both_xor) == 0:
        rightmost_set_bit = rightmost_set_bit << 1
    num1, num2 = 0, 0
    for num in nums:
        if (num & rightmost_set_bit) != 0:  # the bit is set
            num1 ^= num
        else:  # the bit is not set
            num2 ^= num
    return [num1, num2]


def main():
    print('Single numbers are:' +
          str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()
