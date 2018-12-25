"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


class Solution:
    # o(n^2)
    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s[i] not in s[i+1:] and s[i] not in s[:i]:
                return i
        return -1

    def firstUniqChar(self, s):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l)==1]
        return min(index) if len(index) > 0 else -1


print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("cc"))
print(Solution().firstUniqChar("loveleetcode"))