"""
Given a string, s, that represents a DNA sequence, and a number, k, return all the contiguous sequences (substrings) of length k that occur more than once in the string. The order of the returned subsequences does not matter. If no repeated subsequence is found, the function should return an empty set.

1 <= s.length <= pow(10, 4)
 
s[i] is either A, C, G, or T.
"""

def find_repeated_sequences(s, k):
    """ o((n-k+1) *k)
    """
    result = []
    substr_set = set()
    for i in range(len(s)-k+1):

        for j in range(len(s)):
            if j - i + 1 == k:
                if s[i:j] in substr_set:
                    result.append(s[i:j])
                else:
                    substr_set.add(s[i:j])
            if j - i + 1 > k:
                break
    return result


def find_repeated_sequences_with_rabin_karp_algo(s, k):
    if len(s) <= k:
        return []
    base = 3
    high_place_value = pow(base, k-1)

    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    numbers = []
    for i in range(len(s)):
        numbers.append(mapping.get(s[i]))
    
    hash = 0
    substr_hashes, result = set(), []
    for start in range(len(s)-k+1):
        if start == 0:
            for end in range(k):
                hash = hash * base + numbers[end]
        else:
            hash = (hash - numbers[start-1]) * high_place_value * base + numbers[start+k-1]
        
        if hash in substr_hashes:
            result.append(s[start:start+k])
        substr_hashes.add(hash)
    return result

if __name__ == "__main__":
    inputs_string = ["ACGT", "AGACCTAGAC", "AAAAACCCCCAAAAACCCCCC", "GGGGGGGGGGGGGGGGGGGGGGGGG",
                     "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", "TTTTTGGGTTTTCCA",
                     "AAAAAACCCCCCCAAAAAAAACCCCCCCTG", "ATATATATATATATAT"]
    inputs_k = [3, 3, 8, 12, 10, 14, 10, 6]
    for s, k in zip(inputs_string, inputs_k):
        # print(find_repeated_sequences(s, k))
        print(find_repeated_sequences_with_rabin_karp_algo(s, k))
        print("*************")
    
    
