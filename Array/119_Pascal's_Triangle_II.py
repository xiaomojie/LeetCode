"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # time: O(k+1)
        if rowIndex == 0:
            return [1]

        results = [1, 1]
        i = 2
        while i <= rowIndex:
            results.append(results[0])
            for j in range(1, len(results)-1):
                results[j], results[-1] = results[-1] + results[j], results[j]
            i += 1
        return results

    def getRow1(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # time: O(k)
        results = [0 for i in range(rowIndex+1)]
        results[0] = 1
        for i in range(1, rowIndex+1):
            for j in range(i, 0, -1):
                results[j] = results[j] + results[j-1]
        return results


print(Solution().getRow(4))
print(Solution().getRow1(4))