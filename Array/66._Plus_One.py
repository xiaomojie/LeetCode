"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = digits[-1] + 1
        quotient = sum // 10
        digits[-1] = sum % 10
        i = len(digits)-2
        while quotient != 0 and i >= 0:
            sum = digits[i] + quotient
            quotient = sum // 10
            digits[i] = sum % 10
            i -= 1
        if quotient != 0:
            digits = [quotient] + digits
        return digits
print(Solution().plusOne([9,9]))
