"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # backtracking
        def generate(p, left, right, res = []):
            if left:
                generate(p+'(', left-1, right)
            if right > left:
                generate(p+')', left, right-1)
            if not right:
                res.append(p)
            return res

        return generate("", n, n)
