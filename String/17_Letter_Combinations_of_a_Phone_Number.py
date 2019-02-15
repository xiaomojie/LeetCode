"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
               '6': 'mno', '7':'pqrs', '8':'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(map.get(digits[0]))
        pre = self.letterCombinations(digits[0:-1])
        addition = map.get(digits[-1])
        return [p + c for p in pre for c in addition]