"""
if n is even divide by 2
if n is odd multiple by 3  + 1

get the values in each steps
"""

def main(n):
    while True:
        print(n, end=" ")
        if n == 1:
            break
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    print("\n")

n = int(input())
main(n)