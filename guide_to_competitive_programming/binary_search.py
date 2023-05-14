""" find an element target in a sorted array
    O(logn)
    divides the array / 2 every time and hence does only O (logn) searches only
"""




def binary_search(l, h, array, target):
    if l < h:
        mid = (l + h) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            return binary_search(mid+1, h, array, target)
        else:
            return binary_search(l, mid-1, array, target)
    if l == len(array):
        return -1
    return l


def binary_search_1(array, target):
    l = 0
    r = len(array)-1
    while l <= r:
        mid = (l + r) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1




print(binary_search(0, 9, [1,2,3,4,5,6,7,8,9], 4))
print(binary_search(0, 9, [1,2,3,4,5,6,7,8,9], 10))
print(binary_search(0, 9, [1,2,3,4,5,6,7,8,9], 9))

print(binary_search_1([1,2,3,4,5,6,7,8,9], 4))
print(binary_search_1([1,2,3,4,5,6,7,8,9], 10))
print(binary_search_1([1,2,3,4,5,6,7,8,9], 9))