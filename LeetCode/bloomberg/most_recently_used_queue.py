"""
Design Most Recently Used Queue

Design a queue-like data structure that moves the most recently used element to the end of the queue.

Implement the MRUQueue class:

MRUQueue(int n) constructs the MRUQueue with n elements: [1,2,3,...,n].
int fetch(int k) moves the kth element (1-indexed) to the end of the queue and returns it.


Input:
["MRUQueue", "fetch", "fetch", "fetch", "fetch"]
[[8], [3], [5], [2], [8]]
Output:
[null, 3, 6, 2, 2]

Explanation:
MRUQueue mRUQueue = new MRUQueue(8); // Initializes the queue to [1,2,3,4,5,6,7,8].
mRUQueue.fetch(3); // Moves the 3rd element (3) to the end of the queue to become [1,2,4,5,6,7,8,3] and returns it.
mRUQueue.fetch(5); // Moves the 5th element (6) to the end of the queue to become [1,2,4,5,7,8,3,6] and returns it.
mRUQueue.fetch(2); // Moves the 2nd element (2) to the end of the queue to become [1,4,5,7,8,3,6,2] and returns it.
mRUQueue.fetch(8); // The 8th element (2) is already at the end of the queue so just return it.


1 <= n <= 2000
1 <= k <= n
At most 2000 calls will be made to fetch.
"""
import math
import bisect
from sortedcontainers import SortedList


class MRUQueue:

    def __init__(self, n: int):
        self.data = list(range(1, n+1))

    def fetch(self, k: int) -> int:
        self.data.append(self.data.pop(k-1))
        return self.data[-1]
        



class MRUQueue:

    def __init__(self, n: int):
        self.data = SortedList((i, i) for i in range(1, n+1))

    def fetch(self, k: int) -> int:
        _, x = self.data.pop(k-1)
        i = self.data[-1][0] + 1 if self.data else 0
        self.data.add((i, x))
        return x



class MRUQueue:

    def __init__(self, n: int):
        self.n = n
        self.sq_n = int(math.sqrt(n))
        self.data = []
        self.index = []
        for i in range(1, n+1):
            sq_i =(i-1) // self.sq_n
            if sq_i == len(self.data):
                self.data.append([])
                self.index.append(i)
            self.data[-1].append(i)


    def fetch(self, k: int) -> int:
        i = bisect.bisect_right(self.index, k) - 1
        x = self.data[i].pop(k-self.index[i])
        for sq_i in range(i+1, len(self.index)):
            self.index[sq_i] -= 1
        
        if len(self.data[-1]) >= self.sq_n:
            self.data.append([])
            self.index.append(self.n)
        self.data[-1].append(x)
        if not self.data[i]:
            self.data.pop(i)
            self.index.pop(i)
        return x


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)