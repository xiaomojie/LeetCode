"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

class Solution:

    #  Time Limit Exceeded  O(k*n)
    # def containsNearbyDuplicate(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: bool
    #     """
    #     if k >= len(nums):
    #         k = len(nums)-1
    #     for i in range(len(nums)):
    #         j = i + 1
    #         while j <= i + k and j < len(nums):
    #             if nums[i] == nums[j]:
    #                 return True
    #             j += 1
    #     return False

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False

nums = [1,2,3,1,2,3]
k = 2
print(Solution().containsNearbyDuplicate(nums, k))
