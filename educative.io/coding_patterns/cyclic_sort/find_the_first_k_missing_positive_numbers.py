"""
For a given unsorted array, find the first k missing positive numbers in that array.
"""


def first_k_missing_numbers(arr, k):
    n = len(arr)
    i = 0
    while i < n:
        j = arr[i] - 1
        if 0 < arr[i] <= n and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    missing = []
    other_numbers = set()
    i = 0
    while i < n and len(missing) < k:
        if arr[i] != i+1:
            missing.append(i+1)
            other_numbers.add(arr[i])
        i += 1
    j = i
    while len(missing) < k:
        if j+1 not in other_numbers:
            missing.append(j+1)
        j += 1


    return missing




   