"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
import collections


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_s = collections.Counter(s)
        # print(hash_s)
        count = 0
        flag = False
        for x in hash_s.values():
            if x % 2 == 0:
                count += x
            else:
                if not flag:
                    count += 1
                    flag = True
                count += x - 1
        return count

    def longestPalindrome1(self, s):
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)
print(Solution().longestPalindrome("abccccdd"))