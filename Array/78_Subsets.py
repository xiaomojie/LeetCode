"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results, templist = [], []
        for i in range(len(nums) + 1):
            self.backtrack(results, templist, nums, i, 0)
        return results

    def backtrack(self, results, templist, candidates, remain, start):
        length = remain
        if length == 0:
            results.append(list(templist))
        else:
            for i in range(start, len(candidates)):
                templist.append(candidates[i])
                length -= 1
                self.backtrack(results, templist, candidates, length, i+1)
                templist.pop()
                length = remain

nums = [1,2,3,4]
print(Solution().subsets(nums))