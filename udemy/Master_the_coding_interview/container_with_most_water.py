"""
Given an array of integers representing an elevation map where the width of each bar is 1
return how much rainwater can be trapped
"""


def container_with_most_water(height):
    max_area = 0
    n = len(height)
    for i in range(n):
        for j in range(i+1, n):
            print(min(height[i], height[j]) * (j-i))
            max_area = max(max_area, min(height[i], height[j]) * (j-i))
        # print(max_area)
        print("**************************")
    return max_area


# array = [7, 1, 2, 3, 9]
# print(trapping_rain_water(array))
array = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapping_rain_water(array))




