
class Rectangle:
    count = 0
    
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        Rectangle.count += 1

    def __str__(self):
        return "{}, {}".format(
            self.length, self.breadth)

    def area(self):
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


R1 = Rectangle(1, 2)
print R1
L = [10, 20]
print L
s = set()
print s
a = R1.area()
print "area=", a
p = R1.perimeter()
print "perimeter=", p
if R1.issquare():
    print "square"
else:
    print "not a square"

R2 = Rectangle(1, 2)

R3 = R1 + R2


if R1 == R2:
    print "same"
else:
    print "not same"

print R3
print R1.getcount()
