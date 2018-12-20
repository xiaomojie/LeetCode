"""
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
"""


class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(len(M[0]))] for j in range(len(M))]
        for row in range(len(M)):
            for col in range(len(M[0])):
                sum = 0
                count = 0
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if 0 <= row + i < len(M) and 0 <= col + j < len(M[0]):
                            sum += M[row + i][col + j]
                            count += 1
                # print(row, col)
                res[row][col] = sum//count
                # print(res)

        return res
M = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
print(Solution().imageSmoother(M))


