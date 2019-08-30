"""
This is my module contains following services
    data: version
    functions: say_hi
    classes: Person, Employee, Rectangle
"""

version = 1.8
L = [10, 20, 30]


def say_hi():
    print "Hello"


class Person:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def __str__(self):
        return "Person {0},{1},{2}".format(
            self.fname,
            self.lname,
            self.email)

    def fullname(self):
        return self.fname + self.lname

    def getemail(self):
        return self.email


class Employee(Person):
    def __init__(self, fname, lname, email, eid, salary):
        Person.__init__(self, fname, lname, email)
        self.eid = eid
        self.salary = salary

    def __str__(self):
        return "Person {0}, {1}, {2}, {3}, {4}".format(
            self.fname,
            self.lname,
            self.email,
            self.eid,
            self.salary)

    def getsalary(self):
        return self.salary


class Rectangle:
    """
        This is Rectangle class
    """
    count = 0
    
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        Rectangle.count += 1

    def __str__(self):
        return "{}, {}".format(
            self.length, self.breadth)

    def area(self):
        """ 
            This is area function of rectangle
        """
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def issquare(self):
        return self.length == self.breadth

    def scale(self, length=0, breadth=0):
        new_length = self.length + length
        if new_length > 0:
            self.length = new_length
        new_breadth = self.breadth + breadth
        if new_breadth > 0:
            self.breadth = new_breadth

    def __add__(self, other):
        t = Rectangle(self.length + other.length, self.breadth + other.breadth)
        return t

    def __eq__(self, other):
        return self.length == other.length and self.breadth == other.breadth

    def getcount(self):
        return Rectangle.count