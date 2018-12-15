"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]

        results = [[1], [1, 1]]
        i = 3
        while i <= numRows:
            print(i)
            templist = [1 for i in range(i)]
            j = 1
            while j < i - 1:
                templist[j] = results[-1][j-1] + results[-1][j]
                j += 1
            results.append(templist)
            i += 1
        return results

print(Solution().generate(5))