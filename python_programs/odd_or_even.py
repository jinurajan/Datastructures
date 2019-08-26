"""
Write a script to find a given integer is even or odd
"""


def odd_or_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


if __name__ == "__main__":
    print "Enter Number:"
    number = raw_input()
    print odd_or_even(int(number))
