"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


class Solution(object):
    # space: O(m*n)
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        path = [[0]*n for i in range(m)]
        path[0][0] = grid[0][0]
        for i in range(1, n):
            path[0][i] = path[0][i-1] + grid[0][i]
        for i in range(1, m):
            path[i][0] = path[i-1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                path[i][j] = min(path[i-1][j], path[i][j-1]) + grid[i][j]

        return path[m-1][n-1]

    # space: O(2m)
    def minPathSum1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        pre = [grid[0][0] for i in range(m)]
        cur = [0 for i in range(m)]

        for i in range(1, m):
            pre[i] = pre[i-1] + grid[i][0]

        for i in range(1, n):
            cur[0] = pre[0] + grid[0][i]
            for j in range(1, m):
                cur[j] = min(cur[j-1], pre[j]) + grid[j][i]
            pre = cur

        return pre[m-1]

    # space: O(m)
    def minPathSum2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        cur = [grid[0][0] for i in range(m)]

        for i in range(1, m):
            cur[i] = cur[i-1] + grid[i][0]

        for i in range(1, n):
            cur[0] += grid[0][i]
            for j in range(1, m):
                cur[j] = min(cur[j-1], cur[j]) + grid[j][i]

        return cur[m-1]

a = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

print(Solution().minPathSum(a))
print(Solution().minPathSum1(a))

