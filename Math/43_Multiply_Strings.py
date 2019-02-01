"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        product = [0] * (len(num1) + len(num2))
        pos = len(product) - 1

        for i in reversed(num1):
            tmp = pos
            for j in reversed(num2):
                product[tmp] += int(i) * int(j)
                product[tmp - 1] += product[tmp]//10
                product[tmp] %= 10
                tmp -= 1
            pos -= 1
        pt = 0
        while pt < len(product)-1 and product[pt] == 0:
            pt += 1
        # return ''.join([str[i] for i in product[pt:]])
        return ''.join(map(str, product[pt:]))
