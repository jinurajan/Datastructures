"""
Exclusive Execution Time of Functions


We are given an integer number, n, representing the number of functions running in a single-threaded CPU, and an execution log, which is essentially a list of strings. Each string has the format {function id}:{"start" | "end"}:{timestamp}, indicating that the function with function id either started or stopped execution at the time identified by the timestamp value. Each function has a unique ID between 
0 and n-1. Compute the exclusive time of the functions in the program.
"""

from logs import *
from stack import *
from collections import deque


class Log:
    def __init__(self, content):
        content = content.replace(' ', '')
        content = content.split(":")
        self.id = int(content[0])
        self.is_start = content[1] == "start"
        self.time = int(content[2])


# Tip: You may use some of the code templates provided
# in the support files

def exclusive_time(n, logs):
    # Your code will replace this placeholder return statement
    stack = []
    result = [0] * n

    for content in logs:
        log = Log(content)
        if log.is_start:
            stack.append(log)
        else:
            top = stack.pop()
            wait_time = (log.time - top.time+1)
            result[top.id] += wait_time
            if stack:
                result[stack[-1].id] -= wait_time
    return result
