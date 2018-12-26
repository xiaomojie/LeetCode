"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
"""

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # print(row, col)
                if grid[row][col] == 1:
                    adj = (row-1, col), (row+1, col), (row, col-1), (row, col+1)
                    for x, y in adj:
                        if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]) or grid[x][y] == 0:
                            res += 1
        return res


grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
print(Solution().islandPerimeter(grid))

