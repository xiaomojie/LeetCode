"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""

class Solution(object):
    def isPowerOfThree1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3**19 % n == 0

    def isPowerOfThree3(self, n):
        if n > 1:
            while n % 3 == 0:
                n //= 3
        return n == 1

    def isPowerOfThree2(self, n):
        return n > 0 and (n == 1 or (n % 3 == 0 and self.isPowerOfThree2(n/3)))

