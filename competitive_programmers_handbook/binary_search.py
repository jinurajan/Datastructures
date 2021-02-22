

def binary_search_1(array, start, end, x):
    if start <= end:
        mid = (start+end) // 2
        if array[mid] == x:
            return True
        elif array[mid] > x:
            return binary_search_1(array, start, mid-1, x)
        else:
            return binary_search_1(array, mid+1, end, x)
    return False



def binary_search_2(array, x):
    start = 0
    end = len(array)-1
    while start<=end:
        mid = (start + end) // 2
        if array[mid] == x:
            return True
        elif array[mid] > x:
            end = mid -1
        else:
            start = mid + 1
    return False


def binary_search_3(array, x):
    k = 0
    n = len(array)
    start = n // 2
    while start >= 1:
        while start+k < n and array[k+start] <= x:
            k += start
        start //= 2
    if array[k] == x:
        return True
    return False



a = [1,2,3,4,6, 7, 8]
print(binary_search_1(a, 0, len(a)-1, 8))
print(binary_search_1(a, 0, len(a)-1, 10))
print(binary_search_2(a, 8))
print(binary_search_2(a, 10))
print(binary_search_3(a, 8))
print(binary_search_3(a, 10))