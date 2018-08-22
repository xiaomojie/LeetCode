"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""

# time: O(log m*n)
# spam: O(1)
# also can treat the matrix as an array of m*n, then use binary search, the time complexity is also O(log m*n)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if target in matrix[mid]:
                left = 0
                right = len(matrix[mid]) - 1
                while left <= right:
                    row_mid = (left + right) // 2
                    if target == matrix[mid][row_mid]:
                        return True
                    elif target > matrix[mid][row_mid]:
                        left = row_mid + 1
                    else:
                        right = row_mid - 1
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                right = mid - 1
        return False


# matrix  = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
matrix = [[]]
target = 1
print(Solution().searchMatrix(matrix, target))