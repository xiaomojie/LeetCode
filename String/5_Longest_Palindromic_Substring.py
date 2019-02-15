"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(len(s)):
            # 判断以i为中心的奇数型的子串是否是回文，如“aba”
            tmp = self.helper(s, i, i)
            if len(tmp) >= len(res):
                res = tmp
            # 判断以i和i+1为中心的偶数型的子串是否是回文，如“abba”
            tmp = self.helper(s, i, i + 1)
            if len(tmp) >= len(res):
                res = tmp
        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]