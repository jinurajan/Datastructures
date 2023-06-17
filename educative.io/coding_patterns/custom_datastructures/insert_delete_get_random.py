"""
Implement a Random Set data structure that can perform the following operations:


Constructor(): This initializes the Random Set object.
Insert(): This function takes an integer, data, as its parameter and, if it does not already exist in the set, add it to the set, returning TRUE. If the integer already exists in the set, the function returns FALSE
Delete(): This function takes an integer, data, as its parameter and, if it exists in the set, removes it, returning TRUE. If the integer does not exist in the set, the function returns FALSE.
GetRandom(): This function takes no parameters. It returns an integer chosen at random from the set.

"""

from random import choice

class RandomSet():
    def __init__(self):
        """
        Initialize our data structure here.
        """
        self.indexor = {}
        self.store = []

    def insert(self, val):
        """
        Inserts a value in the data structure.
        Returns True if it did not already contain the specified element.
        """
        if val in self.indexor:
            return False
        self.indexor[val] = len(self.store)
        self.store.append(val)
        return True

    def delete(self, val):
        """
        Removes a value from the data structure.
        Returns True if it contained the specified element.
        """
        if val in self.indexor:
            last, i = self.store[-1], self.indexor[val]
            self.store[i], self.indexor[val] = last, i

            del self.indexor[val]
            self.store.pop()
            return True
        return False

    def get_random(self):
        """
        Choose an element at random from the data structure.
        """
        return choice(self.store)