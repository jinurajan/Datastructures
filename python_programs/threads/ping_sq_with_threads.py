import time, os, re, sys
from threading import Thread, Lock


pat = re.compile('r (\d) received')
report = ("No Response", "Partial Response", "Alive")


def computing_time(host, lock):
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


class PingWorker(Thread):
    def __init__(self, lock, host):
        Thread.__init__(self)
        self.lock = lock
        self.host = host

    def run(self):
        # call the computing time
        return computing_time(self.host, self.lock)


print "Without Using Threads"
print "_______________________________________"
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
print "_______________________________________"


print "With Using Threads"
print "_______________________________________"

print time.ctime()
lock = Lock()


threads = [PingWorker(lock, host) for host in range(60, 70)]

[thread.start() for thread in threads]

[thread.join() for thread in threads]

print time.ctime()

print "_______________________________________"
