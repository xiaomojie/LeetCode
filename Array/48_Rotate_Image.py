# -*- coding:utf-8 -*-
"""

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""
import numpy


class Solution(object):
    """
    clockwise rotate
    first reverse up to down, then swap the symmetry
     1 2 3     7 8 9     7 4 1
     4 5 6  => 4 5 6  => 8 5 2
     7 8 9     1 2 3     9 6 3

    """
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # Time:  O(n^2)
        # Space: O(1)
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # Time:  O(n^2)
        # Space: O(n^2)
        matrix[::] = zip(*matrix[::-1])
    """
    
      anticlockwise rotate
      first reverse left to right, then swap the symmetry
      1 2 3     3 2 1     3 6 9
      4 5 6  => 6 5 4  => 2 5 8
      7 8 9     9 8 7     1 4 7
    
    """
    def anti_rotate(self, matrix):
        if not matrix:
            return

        matrix = numpy.array(matrix)
        for i in range(len(matrix[0])//2):
            # 有问题，不是在matrxi上面改的，导致结果不对
            temp = list(matrix[:, i])
            matrix[:, i] = matrix[:, len(matrix) - 1 - i]
            matrix[:, len(matrix) - 1 - i] = temp
            # numpy.array()才能使用[:,i], 或者[x[0] for x in matrix]
            #matrix[:][i],  matrix[:][len(matrix) - 1 - i] = matrix[:][len(matrix) - 1 - i],  matrix[:][i]
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[i])):
                temp = int(matrix[i][j])
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

    def anti_rotate1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[::] = reversed(list(zip(*matrix)))


matrix = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(matrix)
print(matrix)
Solution().rotate1(matrix)
print(matrix)

Solution().anti_rotate1(matrix)
print(matrix)
# Solution().anti_rotate(matrix)
# print(matrix)

