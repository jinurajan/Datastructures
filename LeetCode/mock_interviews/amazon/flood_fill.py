"""
Flood Fill

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""
from typing import List

from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        if not rows:
            return image
        cols = len(image[0])
        q = deque([(sr, sc)])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        while q:
            l = len(q)
            x, y = q.pop()
            visited.add((x, y))
            for idx, idy in neighbors:
                new_x, new_y = x + idx, y + idy
                if (new_x, new_y) in visited:
                    continue
                if 0 <= new_x <= rows - 1 and 0 <= new_y <= cols - 1:
                    if image[new_x][new_y] == image[x][y]:
                        q.append((new_x, new_y))
            image[x][y] = newColor
        return image


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image

        def dfs(x, y):
            if image[x][y] == color:
                image[x][y] = newColor
                if x >= 1:
                    dfs(x - 1, y)
                if x + 1 < rows:
                    dfs(x + 1, y)
                if y >= 1:
                    dfs(x, y - 1)
                if y + 1 < cols:
                    dfs(x, y + 1)

        dfs(sr, sc)
        return image
