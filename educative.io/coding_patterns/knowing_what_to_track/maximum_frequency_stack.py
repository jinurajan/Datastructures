"""
Design a stack-like data structure. You should be able to push elements to this data structure and pop elements with maximum frequency.

You’ll need to implement the FreqStack class that should consist of the following:

Init(): This is a constructor used to declare a frequency stack.

Push(value): This is used to push an integer data onto the top of the stack.

Pop(): This is used to remove and return the most frequent element in the stack.
"""

from collections import defaultdict

class FreqStack:
    # Use constructor to initialize the FreqStack object
    def __init__(self):
        self.frequency = defaultdict(int)
        self.group = defaultdict(list)
        self.max_frequency = 0


    # Use push() function to push the element into the stack
    def push(self, value):
        freq = self.frequency[value] + 1
        self.frequency[value] = freq
        self.max_frequency = max(self.max_frequency, freq)
        self.group[freq].append(value)
        

    # Use pop() function to pop the most frequent element from the stack
    def pop(self):
        if self.max_frequency > 0:
            value = self.group[self.max_frequency].pop()
            self.frequency[value] -= 1
            if not self.group[self.max_frequency]:
                self.max_frequency -= 1
            return value
        return -1
       
