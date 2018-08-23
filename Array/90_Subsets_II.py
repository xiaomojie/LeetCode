"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        templist = []
        for i in range(len(nums) + 1):
            self.backtrack(results, templist, nums, i, 0)
        return results

    def backtrack(self, results, templist, nums, remain, start):
        if remain == 0:
            results.append(list(templist))
        else:
            i = start
            while i < len(nums):
                templist.append(nums[i])
                self.backtrack(results, templist, nums, remain-1, i+1)
                templist.pop()
                j = i + 1
                while j < len(nums) and nums[j] == nums[i]:
                    j += 1
                i = j

nums = [1,4,4,4]
print(Solution().subsetsWithDup(nums))

