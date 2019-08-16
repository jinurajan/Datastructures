# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    number_of_digits = len(str(N))
    if number_of_digits == 1:
        return 0
    return 10 ** (number_of_digits - 1)




print solution(125)
print solution(10)
print solution(1)
print solution(1224252)