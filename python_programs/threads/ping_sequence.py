import os
import re
import time
import sys

pat = re.compile('r (\d) received')
report = ("No Response", "Partial Response", "Alive")


print time.ctime()

for host in range(60, 70):
    ip = "192.168.200." + str(host)
    channel = os.popen("ping -q -c2 " + ip, 'r')
    print "Testing....", ip
    sys.stdout.flush()
    while True:
        line = channel.readline()
        if not line:
            break
        result = re.findall(pat, line)
        if result:
            print report[int(result[0])]


print time.ctime()
