"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for word in strs:
            # key = tuple(sorted(word))
            key = ''.join(sorted(word))
            d[key] = d.get(key, [])+[word]
        return list(d.values())


# print(tuple(sorted("12")))
print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
