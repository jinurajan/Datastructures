"""
You’re given a nested list of integers. Each element is either an integer or a list whose elements may also be integers or other integer lists. Your task is to implement an iterator to flatten the nested list.

You will have to implement the Nested Iterator class. This class has the following functions:

Constructor: This initializes the iterator with the nested list.
Next (): This returns the next integer in the nested list.
Has Next (): This returns TRUE if there are still some integers in the nested list. Otherwise, it returns FALSE.
"""


class NestedIntegers:
    # Constructor initializes a single integer if a value has been passed
    # else it initializes an empty list
    def __init__(self, integer=None):
        if integer:
            self.integer = integer
        else:
            self.n_list = []
            self.integer = 0 

    # If this NestedIntegers holds a single integer rather 
    # than a nested list, returns TRUE, else, returns FALSE
    def is_integer(self):
        if self.integer:
            return True
        return False

    # Returns the single integer, if this NestedIntegers holds a single integer
    # Returns null if this NestedIntegers holds a nested list
    def get_integer(self):
        return self.integer

    #  Sets this NestedIntegers to hold a single integer.
    def set_integer(self, value):
        self.n_list = None
        self.integer = value

    # Sets this NestedIntegers to hold a nested list and adds a nested 
    # integer to it.
    def add(self, ni):
        if self.integer:
            self.n_list = [] 
            self.n_list.append(NestedIntegers(self.integer)) 
            self.integer = None
        self.n_list.append(ni) 

    # Returns the nested list, if this NestedIntegers holds a nested list 
    # Returns null if this NestedIntegers holds a single integer
    def get_list(self):
        return self.n_list



class NestedIterator:
    # Initializes the NestedIterator with nested_list
    def __init__(self, nested_list):
        # Write code here
        self.stack = list(reversed(nested_list))

    # checks if there are still some integers in nested_list
    def has_next(self):
        # Write code here
        while self.stack:
            top = self.stack[-1]
            if top.is_integer():
                return True
            top_list = self.stack.pop().get_list()
            i = len(top_list) -1
            while i >= 0:
                self.stack.append(top_list[i])
                i -= 1
        return False

    # returns the next element from nested_list
    def next(self): 
        if self.has_next():
            return self.stack.pop().get_integer()
        return None


# ------ Please don't change the following function ----------
# flatten_list function is used for testing porpuses.
# Your code will be tested using this function
def flatten_list(nested_iterator_object):
    result = []
    while nested_iterator_object.has_next():
        result.append(nested_iterator_object.next()) 
    return result