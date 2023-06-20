"""
Number of Ships in a Rectangle


Each ship is located at an integer point on the sea represented by a cartesian plane, and each integer point may contain at most 1 ship.

You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true If there is at least one ship in the rectangle represented by the two points, including on the boundary.

Given two points: the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle. It is guaranteed that there are at most 10 ships in that rectangle.

Submissions making more than 400 calls to hasShips will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.
"""

# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
class Point:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        count = 0
        
        if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
            return 0
        
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        
        mx = (topRight.x + bottomLeft.x) // 2
        
        my = (topRight.y + bottomLeft.y) // 2
        
        count = 0
        
        count += self.countShips(sea, topRight, Point(mx+1, my+1))
        count += self.countShips(sea, Point(topRight.x, my), Point(mx+1, bottomLeft.y) )
        
        count += self.countShips(sea, Point(mx, topRight.y), Point(bottomLeft.x, my+1) )
        count += self.countShips(sea, Point(mx,my),  bottomLeft)
        
        return count
        