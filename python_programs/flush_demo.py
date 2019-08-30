"""
    \n is the indicator to flush out the buffer
    if , is added to the print it accumulates
    or if the buffer is full then it flushes
"""
import time
import sys

for i in range(10):
    print '......',
    sys.stdout.flush()
    time.sleep(1)
