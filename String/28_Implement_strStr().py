"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


class Solution(object):
    def strStr1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1 = len(haystack)
        l2 = len(needle)
        if l1 < l2:
            return -1
        elif l2 == 0:
            return 0

        diff = l1 - l2
        i = 0
        while i <= diff:
            if haystack[i: i+l2] == needle:
                return i
            i += 1
        return -1

    def strStr(self, haystack, needle):
        i = 0
        while True:
            j = 0
            while True:
                if j == len(needle):
                    return i
                if i + j == len(haystack):
                    return -1
                if haystack[i+j] != needle[j]:
                    break
                j += 1
            i += 1

print(Solution().strStr("mississippi", "issipi"))
# print(Solution().strStr("hello", "ll"))
