"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.
"""

class Solution:
    # time limited
    def nthUglyNumber1(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            res += 1
            num = res
            factors = [2, 3, 5]
            for f in factors:
                while num % f == 0:
                    num /= f
            if num == 1:
                n -= 1
        return res

    def nthUglyNumber(self, n):



print(Solution().nthUglyNumber(406))
