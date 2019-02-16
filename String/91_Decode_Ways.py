"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<1:
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, len(s) + 1):
            first = s[i-1:i]
            second = s[i-2:i]
            if 0 < int(first) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(second) <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]
