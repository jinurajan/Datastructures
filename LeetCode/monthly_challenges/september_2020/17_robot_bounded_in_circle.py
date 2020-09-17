"""
Robot Bounded In Circle

On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:

Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.
Example 3:

Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 

Note:

1 <= instructions.length <= 100
instructions[i] is in {'G', 'L', 'R'}
"""


class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x, y = 0, 0
        dx, dy = 0, 1
        for i in 4 * instructions:
            if i == 'G':
                x, y = x + dx, y+dy
            elif i == 'L':
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx

        return (x, y) == (0, 0)



class Solution1(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        dx, dy = 0, 1
        x, y = 0, 0
        for i in instructions:
            if i == 'G':
                x, y = x + dx, y+dy
            elif i == 'L':
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx

        return (x, y) == (0, 0) or (x, y) == (0, 1)


print Solution().isRobotBounded("GGLLGG") == True
print Solution().isRobotBounded("GG") == False
print Solution().isRobotBounded("GL")

print Solution1().isRobotBounded("GGLLGG") == True
print Solution1().isRobotBounded("GG") == False
print Solution1().isRobotBounded("GL")





                