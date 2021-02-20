"""
Merge Sort
"""



def merge(array1, array2):
    result = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1

    result.extend(array1[i:])
    result.extend(array2[j:])
    return result


def mergesort(array, start, end):
    if start < end:
        mid = (start + end) // 2
        left = mergesort(array, start, mid)
        right = mergesort(array, mid+1, end)
        return merge(left, right)
    return array[start:end+1]


array = [1, 4, 2, 3, 5, 6, 8, 7]
import pdb; pdb.set_trace()
print(mergesort(array, 0, len(array)-1))