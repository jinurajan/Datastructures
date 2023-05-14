""""""



def merge_sort(lower, upper, array):
    if lower < upper:
        mid = (lower + upper) // 2
        l = merge_sort(lower, mid, array)
        r = merge_sort(mid+1, upper, array)
        return merge(l, r)
    return array[lower:upper+1]


def merge(array1, array2):
    print(array1, array2)
    result = []
    l1, l2 = 0, 0
    n1, n2 = len(array1), len(array2)
    while l1 < n1 and l2 < n2:
        if array1[l1] <= array2[l2]:
            result.append(array1[l1])
            l1 += 1
        else:
            result.append(array2[l2])
            l2 += 1
    if l1 < n1:
        result += array1[l1:]
    if l2 < n2:
        result += array2[l2:]
    
    return result


# print(merge([1,3,6,7] , [1, 2, 4, 6, 7]))
# print(merge([] , [1, 2, 4, 6, 7]))
# print(merge([1,2,3,4] , []))
# print(merge([1,2,3,4] , [5,6,7,8]))

print(merge_sort(0, 7, [1,3,2,4,7,6,6]))
