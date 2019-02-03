"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

class Solution:
    def addDigits1(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num)) > 1:
            total = sum([int(i) for i in str(num)])
            num = total
        return num

    def addDigits(self, num):
        return 1 + (num-1)%9

print(Solution().addDigits(38))

