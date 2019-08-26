"""
Write a script to find smallest integer out of 3 integers
"""


def smallest_of_3(a, b, c):
    smallest = a if a < b else b
    smallest = c if smallest > c else smallest
    return smallest


if __name__ == "__main__":
    print "Enter 3 Numbers:"
    numbers = raw_input().split()
    if len(numbers) != 3:
        raise Exception(
            "Numbers count mismatch:{}".format(
                len(numbers)))
    numbers = [int(n) for n in numbers]
    print smallest_of_3(numbers[0], numbers[1], numbers[2])
