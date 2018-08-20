"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # print(obstacleGrid)
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        path = [[0]*n for i in range(m)]
        path[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] != 1 and path[i-1][0] != 0:
                path[i][0] = 1
        for j in range(1, n):
            if obstacleGrid[0][j] != 1 and path[0][j-1] != 0:
                path[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    path[i][j] = 0
                else:
                    path[i][j] = path[i-1][j] + path[i][j-1]

        return path[m-1][n-1]
a = [[0,0,0],[0,1,0],[0,0,0]]
print(Solution().uniquePathsWithObstacles(a))