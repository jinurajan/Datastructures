
from typing import List
from collections import defaultdict

def generate_permutations(array: List):
    n = len(array)
    result, perm = [], []
    chosen = defaultdict(bool)
    def search():
        if len(perm) == n:
            result.append(perm[:])
        else:
            for i in range(n):
                if chosen[i]:
                    continue
                perm.append(array[i])
                chosen[i] = True
                print(f"calling from loop:{i}")
                search()
                chosen[i] = False
                perm.pop()
    search()
    return result


def generate_permutations_with_swapping(array):
    n = len(array)
    result = []
    def search(index):
        if index == n:
            result.append(array[:])
        else:
            for i in range(index,n):
                array[index], array[i] = array[i], array[index]
                search(index+1)
                array[index], array[i] = array[i], array[index]
    search(0)
    return result



array = [1,2,3]
print(generate_permutations(array))
print(generate_permutations_with_swapping(array))
