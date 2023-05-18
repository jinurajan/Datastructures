"""
Given a string, s, that represents a DNA sequence, and a number, k, return all the contiguous sequences (substrings) of length k that occur more than once in the string. The order of the returned subsequences does not matter. If no repeated subsequence is found, the function should return an empty set.

"""

def find_repeated_sequences(s, k):
    # your code will replace this placeholder return statement
    print(s, k)
    repeated_substrings = set()
    hash_set = set()
    start = 0
    end = 0
    prev_char = None
    curr_hash = None
    while end < len(s):
        if end - start + 1 == k:
            curr_hash = get_hash(prev_char, curr_hash, s[start:end+1], k)
            if curr_hash in hash_set:
                repeated_substrings.add(s[start:end+1])
            else:
                hash_set.add(curr_hash)
            prev_char = s[start]
            start += 1
        end += 1
    return list(repeated_substrings)


def get_val(char):
    return ord(char)

PRIME_NUMBER = 3
def get_hash(prev_char, curr_hash, new_str, k):
    if not curr_hash:
        # fresh string compute entire hash
        high_val = k-1
        hash_val = 0
        i = 0
        while i < k:
            hash_val += get_val(new_str[i]) * pow(PRIME_NUMBER, high_val)
            i += 1
            high_val -= 1
        return hash_val
    else:
        curr_hash -= get_val(prev_char) * pow(PRIME_NUMBER, k-1)
        curr_hash *= PRIME_NUMBER
        curr_hash += get_val(new_str[-1])
        return curr_hash



def find_repeated_sequences_simplified(s, k):
    window_size = k
    if len(s) <= window_size:
        return set()

    # parameters of rolling hash
    base = 3        # 'a', the hash parameter
    hi_place_value = pow(base, window_size - 1) # a^(k-1), the highest place value

    # mapping of a character into an integer
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    numbers = []
    for i in range(len(s)):
        numbers.append(mapping.get(s[i]))

    hashing = 0
    substring_hashes, output = set(), set()
    # iterate over all window-sized substrings
    for start in range(len(s) - window_size + 1):
        # hash function of current subsequence
        if start != 0:
            hashing = (hashing - numbers[start - 1] * hi_place_value) * base \
                    + numbers[start + window_size - 1]
        else:
            for end in range(window_size):
                hashing = hashing * base + numbers[end]
        # subsequence and output sets
        if hashing in substring_hashes:
            output.add(s[start:start + window_size])
        substring_hashes.add(hashing)
    return output