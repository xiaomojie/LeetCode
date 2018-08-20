"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not matrix:
            return result
        rowbegin = 0
        rowend = len(matrix) - 1

        colbegin = 0
        colend = len(matrix[0]) - 1

        while rowbegin <= rowend and colbegin <= colend:
            for j in range(colbegin, colend + 1):
                result.append(matrix[rowbegin][j])
            rowbegin += 1

            for j in range(rowbegin, rowend + 1):
                result.append(matrix[j][colend])
            colend -= 1

            if rowbegin <= rowend:
                for j in range(colend, colbegin-1, -1):
                    result.append(matrix[rowend][j])
            rowend -= 1

            if colbegin <= colend:
                for j in range(rowend, rowbegin-1, -1):
                    result.append(matrix[j][colbegin])
            colbegin += 1

        return result

a = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().spiralOrder(a))