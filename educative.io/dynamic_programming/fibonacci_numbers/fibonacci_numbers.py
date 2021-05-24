"""
Write a function to calculate the nth Fibonacci number.

Fibonacci numbers are a series of numbers in which each number is the sum of the two preceding numbers. First few Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, …

Mathematically we can define the Fibonacci numbers as:

    Fib(n) = Fib(n-1) + Fib(n-2), for n > 1

    Given that: Fib(0) = 0, and Fib(1) = 1
"""
def calculateFibonacci(n):
  # TODO: Write your code here
  if n < 2:
    return n
  return calculateFibonacci(n-1) + calculateFibonacci(n-2)


def calculate_fibonacci_topdown(n):
    mem = [-1 for i in range(n+1)]

    def calculate(n):
        if mem[n] != -1:
            return mem[n]
        if n < 2:
            mem[n] = n
        else:
            mem[n] = calculate(n-1) + calculate(n-2)
        return mem[n]
    return calculate(n)


def calculate_fibonacci_bottom_up(n):
    if n < 2:
        return n
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[-1]


def calculate_fibonacci_mem_optimized(n):
    if n < 2:
        return n
    n1, n2, tmp = 0, 1, 0
    for i in range(2, n+1):
        tmp = n1+n2
        n1 = n2
        n2 = tmp
    return n2

print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


print("5th Fibonacci is ---> " + str(calculate_fibonacci_topdown(5)))
print("6th Fibonacci is ---> " + str(calculate_fibonacci_topdown(6)))
print("7th Fibonacci is ---> " + str(calculate_fibonacci_topdown(7)))


print("5th Fibonacci is ---> " + str(calculate_fibonacci_bottom_up(5)))
print("6th Fibonacci is ---> " + str(calculate_fibonacci_bottom_up(6)))
print("7th Fibonacci is ---> " + str(calculate_fibonacci_bottom_up(7)))


print("5th Fibonacci is ---> " + str(calculate_fibonacci_mem_optimized(5)))
print("6th Fibonacci is ---> " + str(calculate_fibonacci_mem_optimized(6)))
print("7th Fibonacci is ---> " + str(calculate_fibonacci_mem_optimized(7)))
