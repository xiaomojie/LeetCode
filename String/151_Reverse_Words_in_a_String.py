"""
Given an input string, reverse the string word by word.

Example:

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return " ".join(s.split()[::-1])
        s = s.split(" ")
        return ' '.join([item for item in s[::-1] if item != ''])


print(Solution().reverseWords("the sky is blue"))

a = "1   2 3"
print(a.split(" "))


a = [1,2,3]
a.reverse()
print(a)

b = "1 23"
b.replace(" ", ",")
print(b)

c = "1 34"
a = c.split(" ")
print(a)