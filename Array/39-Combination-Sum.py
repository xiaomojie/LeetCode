"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 2,3,6,7 and target 7,
# A solution set is:
# [7]
# [2, 2, 3]
#

# Time:  O(k * n^k)
# Space: O(k)
# reference: https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)

class Solution(object):
    def combinationSum(self, candidates, target):
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
        elif remain == 0:
            results.append(list(templist))
        else:
            for i in range(start, len(candidates)):
                templist.append(candidates[i])
                self.backtrack(results, templist, candidates, remain - candidates[i], i)
                templist.pop()


print(Solution().combinationSum([2,3,6,7], 7))
print(Solution().combinationSum([1,2,5], 8))