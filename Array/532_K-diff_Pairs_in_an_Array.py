"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
"""


class Solution:
    def findPairs1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ans = 0
        i = 0
        while i < len(nums)-1:
            j = i + 1
            while j < len(nums):
                if nums[j] - nums[i] == k:
                    ans += 1
                    break
                elif nums[j] - nums[i] > k:
                    break
                j += 1
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return ans

    def findPairs(self, nums, k):
        count = 0
        set_nums = set(nums)
        if k == 0:
            for each in set_nums:
                if nums.count(each) > 1:
                    count += 1
        elif k < 0:
            return 0
        else:
            for i in set_nums:
                if i + k in set_nums:
                    count += 1
        return count