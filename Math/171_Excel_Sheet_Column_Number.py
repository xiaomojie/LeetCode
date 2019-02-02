"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""

class Solution:
    def titleToNumber1(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        while s is not '':
            t = s[0]
            res = res*26 + ord(t) - ord('A') + 1
            s = s[1:]
        return res

print(Solution().titleToNumber('ZY'))
print(ord('A'))