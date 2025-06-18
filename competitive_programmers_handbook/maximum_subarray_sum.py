"""
maximum subarray sum

find the maximum sum of subarray in a array

eg: [-1, 2, 4, -3, 5, 2, -5, 2]
"""



def maximum_subarray_sum_1(array):
    n = len(array)
    best = 0
    for a in range(n):
        for b in range(a, n):
            sum = 0
            for k in range(a, b):
                sum += array[k]
            best = max(sum, best)
    
    return best

def maximum_subarray_sum_2(array):
    n = len(array)
    best = 0
    for a in range(n):
        sum = 0
        for b in range(a, n):
            sum += array[b]
            best = max(sum, best)
    return best


def maximum_subarray_sum_3(array):
    n = len(array)
    best = 0
    sum = 0
    for a in range(n):
        sum = max(array[a], sum+array[a])
        best = max(best, sum)
    return best


if __name__ == "__main__":
    array = [-1, 2, 4, -3, 5, 2, -5, 2]
    print(maximum_subarray_sum_1(array))
    print(maximum_subarray_sum_2(array))
    print(maximum_subarray_sum_3(array))