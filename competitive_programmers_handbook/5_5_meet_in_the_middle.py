"""
we are given a list of n numbers and a number x, and we want to find out if it is possible to choose some numbers from the list so that their sum is x. For example, given the list [2,4,5,9] and x=15, we can choose the numbers [2,4,9] to get 2+4+9=15. However, if x=10 for the same list, it is not possible to form the sum

This is a backtracking problem of O(2 raised n)

use bound conditions to optimize this


"""


def sum_exists(num, target):
    n = len(num)
    result = False
    def backtrack(index, sum_1, sum_2):
        nonlocal result
        if sum_1 == target or sum_2 == target:
            result = True
            return
        elif index == n:
            return
        backtrack(index+1, sum_1+num[index], sum_2-num[index])
        backtrack(index+1, sum_1, sum_2 - num[index])
    backtrack(0, 0, sum(num))
    return result


def find_all_unique_combinations(num, target):
    n = len(num)
    result = []
    indices = []
    def backtrack(index, sum_1, sum_2):
        if sum_1 == target or sum_2 == target:
            result.append([num[idx] for idx in indices])
            return
        elif index == n:
            return
        indices.append(index)
        backtrack(index+1, sum_1+num[index], sum_2-num[index])
        indices.pop()
        backtrack(index+1, sum_1, sum_2 - num[index])
    backtrack(0, 0, sum(num))
    return result


array = [5, 10, 12, 13, 15, 18]

print(sum_exists(array, 30))
print(sum_exists(array, 130))
print(find_all_unique_combinations(array, 30))

array = [10,1,2,7,6,1,5]
print(sum_exists(array, 8))
print(find_all_unique_combinations(array, 8))
