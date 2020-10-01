"""
Number of Recent Calls


You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

 

Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
 

Constraints:

1 <= t <= 104
Each test case will call ping with strictly increasing values of t.
At most 104 calls will be made to ping.
"""

class RecentCounterWithArray(object):

    def __init__(self):
        self.q = []
        self.count = 0
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)
        self.count += 1
        while self.q:
            if t - self.q[0] <= 3000:
                break
            self.q.pop(0)
            self.count -= 1
        return self.count



class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class RecentCounterWithLL(object):

    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def ping(self, t):
        new_node = ListNode(t)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = self.last.next
        self.count += 1
        return self.clean_up_old(t)

    def clean_up_old(self, t):
        if not self.first:
            return 0
        if t - self.first.val > 3000:
            self.count -= 1
            self.first = self.first.next
            return self.clean_up_old(t)
        else:
            return self.count



class Queue(object):
    def __init__(self):
        self.q = []

    def enqueue(self, val):
        self.q.append(val)

    def dequeue(self):
        return self.q.pop(0) if self.q else None

    def is_empty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)

    def get(self):
        return self.q[0]


class RecentCounterWithQueue(object):

    def __init__(self):
        self.requests = Queue()


    def ping(self, t):
        self.requests.enqueue(t)
        while t - self.requests.get() > 3000:
            self.requests.dequeue()
        return self.requests.size()



import collections

class RecentCounter(object):

    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)

# Your RecentCounter object will be instantiated and called as such:
# import pdb; pdb.set_trace()
obj = RecentCounterWithArray()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3002))
print(obj.ping(3003))

print("******")
obj = RecentCounterWithLL()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3002))
print(obj.ping(3003))

print("*****")
obj = RecentCounterWithQueue()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3002))
print(obj.ping(3003))


print("*****")
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3002))
print(obj.ping(3003))

