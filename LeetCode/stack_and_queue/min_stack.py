"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:
Methods pop, top and getMin operations will always be called on non-empty stacks.
"""

from collections import deque


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = deque()
        self.min = 0

    def push(self, x: int) -> None:
        if not self.q:
            self.q.append((x, x))
            self.min = x
        else:
            _, min_val = self.q[-1]
            min_val = min(min_val, x)
            self.q.append((x, min_val))
            self.min = min_val

    def pop(self) -> None:
        if not self.q:
            return
        res, min_val = self.q.pop()
        if not self.q:
            self.min = 0
        else:
            self.min = self.q[-1][1]
        return res

    def top(self) -> int:
        return self.q[-1][0]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()