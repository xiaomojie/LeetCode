"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""

class Solution:
    def convertToTitle1(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''

        while n != 0:
            n -= 1
            res = chr(n % 26 + ord('A')) + res
            n = n // 26
        return res

    def convertToTitle(self, n):
        return "" if n==0 else self.convertToTitle((n-1)//26) + chr((n-1)%26+ord('A'))

print(Solution().convertToTitle(28))