"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
from collections import Counter


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        c_p = Counter(p)
        c_s = Counter(s[:len(p)-1])
        res = []
        for i in range(len(p)-1, len(s)):
            c_s[s[i]] += 1
            if c_p == c_s:
                res.append(i-len(p)+1)
            c_s[s[i-len(p)+1]] -= 1
            if c_s[s[i-len(p)+1]] == 0:
                c_s.pop(s[i-len(p)+1])
                # del c_s[s[i-len(p)+1]]
        return res

print(Solution().findAnagrams("cbaebabacd", "abc"))

