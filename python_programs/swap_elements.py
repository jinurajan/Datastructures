"""
Wirte a script to swap first element with last element, second with second last element and so on 
"""


def swap_elements(array):
    start = 0
    end = len(array)-1
    while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end -= 1
    return array

if __name__ == "__main__":
    print "Enter Array:"
    numbers = raw_input().split()
    inputs = [int(n) for n in numbers]
    print swap_elements(inputs)
