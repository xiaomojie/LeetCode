"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
import numpy


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # results = numpy.zeros([n,n])
        results = [[0 for i in range(n)] for i in range(n)]
        # or results = [[0]*n for i in range(n)]
        # error: [[0]*n]*n   is not a copy reference
        print(results)
        rowbegin = 0
        rowend = n - 1
        colbegin = 0
        colend = n - 1

        num = 1
        while rowbegin <= rowend and colbegin <= colend:
            for i in range(colbegin, colend + 1):
                results[rowbegin][i] = num
                num += 1
            rowbegin += 1
            for i in range(rowbegin, rowend + 1):
                results[i][colend] = num
                num += 1
            colend -= 1

            if rowbegin <= rowend:
                for i in range(colend, colbegin - 1, -1):
                    results[rowend][i] = num
                    num += 1
                rowend -= 1

            if colbegin <= colend:
                for i in range(rowend, rowbegin - 1, -1):
                    results[i][colbegin] = num
                    num += 1
                colbegin += 1
        return results

print(Solution().generateMatrix(3))
