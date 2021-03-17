"""
Generate Random Point in a Circle

Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

Note:

input and output values are in floating-point.
radius and x-y position of the center of the circle is passed into the class constructor.
a point on the circumference of the circle is considered to be in the circle.
randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.
Example 1:

Input:
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

Example 2:

Input:
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. randPoint has no arguments. Arguments are always wrapped with a list, even if there aren't any.

"""
from typing import List

from random import random
from math import sqrt


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self) -> List[float]:
        x0 = self.xc - self.radius
        y0 = self.yc - self.radius
        """
        consider a square covering circle and area will be 2 R * 2R = 4R raised to 2
        area of circle = pi *R raised to 2
        probability of getting uniform distribution = pi * R2 // 4R2 == 3.14 / 4 = .785 ~ 78.5%
        Use euclidean distance of the generated sample to reject it. distance between two points
        are sqroot(x2-x1)**2 + (y2-y1)**2)
        """
        while True:
            xg = x0 + random() * self.radius * 2
            yg = y0 + random() * self.radius * 2
            if sqrt(pow(xg - self.xc, 2) + pow(yg - self.yc, 2)) <= self.radius:
                return (xg, yg)


from random import random
from math import sqrt, pi


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self) -> List[float]:
        """
        find a random length d and an angle

        """
        d = self.radius * sqrt(random())
        theta = random() * 2 * pi
        return (d * cos(theta) + self.xc, d * sin(theta) + self.yc)


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self) -> List[float]:
        """
        find a random length d and an angle from 0-360 degree
        x = x+ distance * cos(theta)
        y = y+ distance * sin(theta)
        """
        d = self.radius * sqrt(random())
        theta = random() * 360
        return (d * cos(theta) + self.xc, d * sin(theta) + self.yc)