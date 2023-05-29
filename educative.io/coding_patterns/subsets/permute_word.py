"""
"""


def permute_word(word):
    result = []
    n = len(word)
    word = list(word)
    def backtrack(index):
        if index == n:
            result.append("".join(word))
        else:
            for i in range(index, n):
                word[index], word[i] = word[i], word[index]
                backtrack(index+1)
                word[index], word[i] = word[i], word[index]
    backtrack(0)
    return result


# This function will swap characters for every permutation
def swap_char(word, i, j):
    swap_index = list(word)
    swap_index[i], swap_index[j] = swap_index[j], swap_index[i]

    return ''.join(swap_index)

# Driver code
def main():

    input_word = ["ab", "bad", "abcd"]
    indexes_to_swap = [(0, 1), (1, 2), (1, 3)]

    for i in range(len(input_word)):
        permuted_words = permute_word(input_word[i])
        print(i + 1, ".\t Input string: '", input_word[i], "'", sep="")
        print("\t Permuted words: ",
              "[", ', '.join(permuted_words), "]", sep="")
        print('-' * 100)


if __name__ == '__main__':
    main()