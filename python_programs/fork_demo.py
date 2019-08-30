# import os, time
# print "hi"
# os.fork()
# print "hello"
# os.fork()
# print "Done"

import os
import time


child = os.fork()
if child == 0:
    # for child to execute
    print "Child started with pid:", os.getpid()
    for i in range(10):
        print "Child: value is", i
        time.sleep(1)
    os._exit(0)
os.wait() # parent will wait until child process is completed
# when you remove the above line context switching happens between the parent and child process
print "PARENT started with PID:", os.getpid()
for j in range(10):
    print "Parent value is", j
    time.sleep(1)
os._exit(0)
