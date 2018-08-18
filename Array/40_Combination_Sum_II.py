"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results, templist = [], []
        candidates.sort()
        self.backtrack(results, templist, candidates, target, 0)
        return results

    def backtrack(self, results, templist, candidates, remain, start):
        if remain < 0:
            return
        if remain == 0:
            results.append(list(templist))
        else:
            i = start
            while i < len(candidates):
                templist.append(candidates[i])
                self.backtrack(results, templist, candidates, remain - candidates[i], i+1)
                templist.pop()
                j = i + 1
                while j < len(candidates) and candidates[j] == candidates[i]:
                    j += 1
                i = j


# print(Solution().combinationSum2( [10,1,2,7,6,1,5], 8))
# print(Solution().combinationSum2( [2,2,2], 2))
print(Solution().combinationSum2( [33,20,22,13,20,15,34,12,27,28,6,32,32,28,12,17,26,23,8,15,33,9,20,26,28,34,31,19,11,5,10,9,13,19,10,28,29,31,27,13,25,28,32,14,14,31,26,27,19,29]
,25))