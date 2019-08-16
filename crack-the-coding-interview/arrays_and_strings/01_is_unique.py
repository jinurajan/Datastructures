"""
Question:
Is Unique: Implement an algorithm to dtermine if a string has all unique characters. What if you
cannot use additional data structures?

Assumptions:
String has only Ascii characters - 128 characters

Note: If the string contains unicode -  used to contain 65,536 till 1.1 version (1993)
But now has 1114112 (17 plane * 65,536). Then this needs to have an array of 1114112 length/ minimum 1114112/8 if using bit vector

Idea:
Solution 1:
step 1: check if length of array is more than 128. If yes its certain that there are duplicates. return false
step 2: Create an array of 128 length and set flag for each characters. If any of the array index true flag already set exit

Time complexity - is constant since length of array is constant ie O(1). (If the character set is  not fixed then O(N) where N is the maximum number of characters in the set)
Space Complexity - is also constant since length of array is constant for any set of strings ie 0(1). (If the character set is  not fixed then O(N) where N is the maximum number of characters in the set)

We can reduce space by using the bit vector. 1 byte == 8 bit -> will need 128/8 bits for this problem.

"""


def is_unique_using_array(string):
    if len(string) > 128:
        return False
    arr = [False] * 128
    for i in range(len(string)):
        val = ord(string[i])
        if arr[val] is True:
            return False
        arr[val] = True
    return True



def is_unique_using_bitvector(string):
    if len(string) > 128:
        return False
    checker = 0
    for i in range(len(string)):
        val = ord(string[i])
        if checker & (1 << val):
            return False
        checker |= 1 << val
    return True



if __name__ == "__main__":
    print is_unique_using_array("abcd")
    print is_unique_using_array("abcda")

    print is_unique_using_bitvector("abcd")
    print is_unique_using_bitvector("abcda")
