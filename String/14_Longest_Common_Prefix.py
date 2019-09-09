"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution(object):
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        res = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(res) != 0:
                res = res[0:len(res)-1]
        return res

    def longestCommonPrefix2(self, strs):
        if len(strs) < 1:
            return ""
        for index, item in enumerate(zip(*strs)):
            if len(set(item)) > 1:
                return strs[0][0:index]
        else:
            return min(strs)

    def longestCommonPrefix(self, strs):
        if len(strs) < 1:
            return ""
        res = min(strs,key=len)
        for i, ch in enumerate(res):
            for other in strs:
                if other[i] != ch:
                    return res[0:i]
        return res



print(Solution().longestCommonPrefix(["flower","flow","flight"]))