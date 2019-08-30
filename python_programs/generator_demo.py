import time
import sys


# def sequence():
#     i = 0
#     while True:
#         i += 1
#         r = yield i
#         if r == -1:
#             i = r

# gen = sequence()
# print type(gen)

# for i in range(50):
#     n = next(gen)
#     print n,
#     if n == 5:
#         gen.send(-1)
#     sys.stdout.flush()
#     time.sleep(1)

def sequence(seed=0):
    i = 0
    if seed == 1:
        i = -1
        a = 2
    while True:
        i += a
        yield i


gen_odd = sequence(1)
gen_even = sequence(2)

for i in range(10):
    n = next(gen_odd)
    print n
    time.sleep(1)
