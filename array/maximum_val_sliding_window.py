# This is Python 2
import sys


def max_in_sliding_window(arr, w):
    LR = []
    RL = []
    max_val = []
    n = len(arr)
    k = n - w + 1
    for i in range(len(arr)):
        if i % w == 1:
            LR[i] = arr[i]
        else:
            LR[i] = max(LR[i - 1], arr[i])
    for i in range(len(array), 0, -1):
        if(i == n):
            RL[i] = arr[i]
        elif(i % w == 0):
            RL[i] = arr[i]
        else:
            RL[i] = max(RL[i + 1], arr[i])

        for i in range(0, k):
            max_val[i] = max(RL[i], LR[i + w - 1])

        for i in range(k):
            print max_val[i]


line = sys.stdin.readline()
line.strip()
inputs = line.split(" ")
window_size = int(inputs[0])
array = [int(i) for i in inputs[1:]]
print window_size, array
max_in_sliding_window(array, window_size)