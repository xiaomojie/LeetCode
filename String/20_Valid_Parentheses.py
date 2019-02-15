"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 下面这种方法是不对的：(){}[]
        # if len(s) % 2 != 0:
        #     return False
        # ls = list(s)
        # print(ls)
        # while len(ls) > 0:
        #     if parentheses.get(ls.pop(0)) != ls.pop(-1):
        #         return False
        # return True

        parentheses = {")":"(", "}":"{", "]":"["}

        # 使用栈
        stack = []
        for p in s:
            # 当没有key=p时，返回的是None
            if len(stack) and parentheses.get(p) == stack[-1]:
                stack.pop()
            else:
                stack.append(p)
        return stack == []

print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("([)]"))

