"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
"""

class Solution:
    def reverseVowels(self, s: 'str') -> 'str':
        list_s = list(s)
        l, r = 0, len(s)-1
        vowels = ['a', 'o', 'e', 'i', 'u']
        while l < r:
            while l < r and list_s[l].lower() not in vowels:
                l += 1
            while l < r and list_s[r].lower() not in vowels:
                r -= 1
            if l < r:
                list_s[l], list_s[r] = list_s[r], list_s[l]
            l += 1
            r -= 1
        return ''.join(list_s)