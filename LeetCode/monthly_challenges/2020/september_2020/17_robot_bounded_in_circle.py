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

        return (x, y) == (0, 0) or (dx, dy) != (0, 1)



class Solution2(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        # 0=N, 1=E, 2=S, 3=W
        direction = 0
        indices = [0,0]
        for i in instructions:
            # spots.add(spot)
            if i == 'L':
                direction = (direction-1) %4
            if i == 'R':
                direction = (direction+1) %4
            if i == 'G':
                if direction == 0:
                    indices = [indices[0], indices[1]+1]
                if direction == 1:
                    indices = [indices[0]+1, indices[1]]
                if direction == 2:
                    indices = [indices[0], indices[1]-1]
                if direction == 3:
                    indices = [indices[0]-1, indices[1]]    
        if indices == [0,0] or direction != 0:
            return True
        return False




print Solution().isRobotBounded("GGLLGG") == True
print Solution().isRobotBounded("GG") == False
print Solution().isRobotBounded("GL") == True
print Solution1().isRobotBounded("LLGRL") == True

print Solution1().isRobotBounded("GGLLGG") == True
print Solution1().isRobotBounded("GG") == False
print Solution1().isRobotBounded("GL") == True
print Solution1().isRobotBounded("LLGRL") == True


print Solution2().isRobotBounded("GGLLGG") == True
print Solution2().isRobotBounded("GG") == False
print Solution2().isRobotBounded("GL") == True
print Solution2().isRobotBounded("LLGRL") == True







                