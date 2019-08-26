"""
To find the smallest integer along with its position from a given list of n integers
"""


def smallest_integer_position(array):
    smallest_integer = None
    smallest_integer_index = None

    for i in range(len(array)):
        if i == 0:
            smallest_integer = array[i]
            smallest_integer_index = i
        else:
            if array[i] < smallest_integer:
                smallest_integer = array[i]
                smallest_integer_index = i
    return smallest_integer, smallest_integer_index


if __name__ == "__main__":
    print "Enter Array:"
    numbers = raw_input().split()
    inputs = [int(n) for n in numbers]
    print smallest_integer_position(inputs)
