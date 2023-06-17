"""
Design a custom stack class, Min Stack, allowing us to push, pop, and retrieve the minimum value in constant time. Implement the following methods for Min Stack:
Constructor: This initializes the Min Stack object.
Pop(): This removes and returns from the stack the value that was most recently pushed onto it.
Push(): This pushes the provided value onto the stack.
Min Number(): This returns the minimum value in the stack in O(1) time.
"""

from stack import MainStack


class MinStack:
    # Initialize min and main stack here
    def __init__(self):
        self.min_stack = []
        self.main_stack = []
       

    # Remove and returns value from the stack
    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()


    # Pushes values into the stack
    def push(self, value):
        self.main_stack.append(value)

        if not self.min_stack or value < self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])
        

    # Returns minimum value from stack
    def min_number(self):
        if not self.min_stack:
            return None
        else:
            return self.min_stack.pop()
        
