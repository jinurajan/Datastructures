import sys

def is_palindrome_permutation(string):
    # Complexity: O(N)
    hash_map = {}
    no_of_spaces = 0
    for each in string:
        character = each.lower()
        if character != " ":
            if character not in hash_map:
                hash_map[character] = 1
            else:
                hash_map[character] += 1
        else:
            no_of_spaces += 1

    array_actual_length = len(string) - no_of_spaces
    if array_actual_length % 2 == 0:
        # hash map should have all even number counts
        for key, value in hash_map.items():
            if value % 2 == 1:
                return False
        return True
    else:
        # hash map can have only one character count has odd
        no_of_odds = 0
        for key, value in hash_map.items():
            if value % 2 == 1:
                no_of_odds += 1
                if no_of_odds > 1:
                    return False
        return True


def is_palindrome_permutation_with_bitvector(string):
    # bit_count = sys.getsizeof(int())
    bit_vector = 0
    for each in string:
        character = ord(each)
        mask = 1 << character
        if bit_vector & mask == 0:
            bit_vector |= mask
        else:
            bit_vector &= ~mask
        # print character, bit_vector
    return is_only_1_bit_set(bit_vector)


def is_only_1_bit_set(bit_vector):
    print bit_vector
    return bit_vector & (bit_vector - 1) == 0


if __name__ == "__main__":
    # print is_palindrome_permutation("Tact Coa")
    print is_palindrome_permutation_with_bitvector("Tact Coa")