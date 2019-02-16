"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for i in range(1, min(4, len(s)-2)):
            for j in range(i+1,min(i+4, len(s)-1)):
                for k in range(j+1, min(j+4, len(s))):
                    s1, s2, s3, s4 = s[:i], s[i:j], s[j:k], s[k:]
                    if self.isvalid(s1) and self.isvalid(s2) and self.isvalid(s3) and self.isvalid(s4):
                        res.append('.'.join([s1, s2, s3, s4]))
        return res

    def isvalid(self, s):
        # print(s[0]==0)
        if (s[0] == '0' and len(s) > 1) or int(s) > 255:
            return False
        return True

# print(Solution().isvalid("011"))
print(Solution().restoreIpAddresses("010010"))
