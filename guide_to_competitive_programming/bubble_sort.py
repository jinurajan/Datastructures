
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        no_change_count = 0
        for j in range(n-1):
            if array[j] < array[j+1]:
                no_change_count += 1
                continue
            array[j], array[j+1] = array[j+1], array[j]
        if no_change_count == n-1:
            break
    return array

# array = [1,3,8,2,9,2,5,6]
array = [1,2,3,4,5,6,7,8,9]
result = bubble_sort(array)
print(array)
print(result)