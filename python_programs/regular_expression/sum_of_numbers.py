import re


def sum_of_numbers(string):
    numbers = find_numbers(string)
    sum_val = 0
    if numbers:
        for n in numbers:
            sum_val += int(n)

    return sum_val


def find_numbers(string):
    pattern = "\d+"
    result = re.findall(pattern, string)
    return result


if __name__ == "__main__":
    print "Enter string:"
    input = raw_input()
    print sum_of_numbers(input)