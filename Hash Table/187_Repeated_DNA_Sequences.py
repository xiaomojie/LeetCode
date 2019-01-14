"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""

class Solution(object):
    def findRepeatedDnaSequences1(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = set()
        dic = dict()
        for i in range(len(s)-9):
            dic[s[i:i+10]] = dic.get(s[i:i+10], 0) + 1
            if dic[s[i:i+10]] > 1:
                res.add(s[i:i+10])
        return list(res)

# table = collections.defaultdict(int)
