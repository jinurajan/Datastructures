"""
you are given an array of positive integers where each integer represents the height of a vertical line
on a chart. Find two lines which together with the x-axis forms a container that would hold the greatest
amount of water. Return the area of water it would hold
"""

def greatest_amount_of_water_1(array):
    """
    T = O(N)
    S = constant

    """
    max_area = 0
    n = len(array)
    for i in range(n):
        for j in range(i+1, n):
            area = min(array[i], array[j]) * (j-i)
            max_area = max(area, max_area)
    return max_area

def greatest_amount_of_water(array):
    l = 0
    r = len(array)-1
    max_area = 0
    while l < r:
        max_area = max(max_area, min(array[l], array[r])*(r-l))
        if array[l] <= array[r]:
            l += 1
        else:
            r -= 1
    return max_area


a = [7, 1, 2, 5, 9]

print(greatest_amount_of_water_1(a))
print(greatest_amount_of_water(a))