"""
1. Implement fibonacci without using memoization
2. Implement fibonacci using memoization

"""

def fibonacci_with_recursion(n):
    if n < 2:
        return n
    return fibonacci_with_recursion(n-1) + fibonacci_with_recursion(n-2)


def fibonacci_without_recursion(n):
    if n < 1:
        return 0
    first, second = 0, 1
    for i in range(n-1):
        first, second = second, first + second
    return second 



mem = {0: 0, 1: 1}

def fibonacci_using_memoization(n):
    if n in mem:
        return mem[n]

    result = fibonacci_using_memoization(n-1) + \
            fibonacci_using_memoization(n-2)
    mem[n] = result
    return result



print fibonacci_with_recursion(6)
print fibonacci_without_recursion(6)
print fibonacci_using_memoization(6)