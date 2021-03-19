"""
generating all subsets of a set of n elements. For example, the subsets of {1, 2, 3} are {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, and {1, 2, 3}.

"""


def generate_subsets(array):
    n = len(array)
    def find_subsets(index, subset):
        if index == n:
            result.append(subset[:])
            return
        subset.append(array[index])
        find_subsets(index+1, subset)
        subset.pop()
        find_subsets(index+1, subset)
    result = []
    find_subsets(0, [])
    return result

print(generate_subsets([1,2,3]))
