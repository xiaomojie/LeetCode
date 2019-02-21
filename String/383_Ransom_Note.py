"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""


class Solution:
    def canConstruct(self, ransomNote: 'str', magazine: 'str') -> 'bool':
        list_ransomNote = list(ransomNote)
        list_magazine = list(magazine)
        for i in range(len(list_ransomNote)):
            if list_ransomNote[i] in list_magazine:
                list_magazine.remove(list_ransomNote[i])
            else:
                return False
        return True
