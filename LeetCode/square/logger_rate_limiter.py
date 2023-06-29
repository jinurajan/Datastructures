"""
Logger Rate Limiter

Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:

Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.


"""

from collections import deque


class Logger:

    def __init__(self):
        self.msg_set = set()
        self.msg_queue = deque()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.msg_queue:
            msg, ts = self.msg_queue[0]
            if timestamp - ts >= 10:
                self.msg_queue.popleft()
                self.msg_set.remove(msg)
            else:
                break
        if message not in self.msg_set:
            self.msg_set.add(message)
            self.msg_queue.append((message, timestamp))

            return True
        else:
            return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)