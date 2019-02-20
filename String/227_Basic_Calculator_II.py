"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += '+0'  # 为了处理s是纯数字的情况
        stack = []
        num = 0
        preOp = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif not s[i].isspace():
                if preOp == '+': stack.append(num)
                elif preOp == '-': stack.append(-num)
                elif preOp == '*': stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                preOp = s[i]
                num = 0
        return sum(stack)

print(Solution().calculate("14-3/2"))