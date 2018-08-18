# -*- coding:utf-8 -*-
"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution(object):
    # 该方法在整个数组都是target的时候，不是logn
    def searchRange1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                i = mid -1
                while i >= 0 and nums[i] == target:
                    i -= 1
                j = mid + 1
                while j < len(nums) and nums[j] == target:
                    j += 1
                return [i+1, j-1]
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return [-1, -1]

    #  O(log n)
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        # 找左边界
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return [-1, -1]
        else:
            i = left
        right = len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        return [i, right]


print(Solution().searchRange([5,7,7,8,8,10], 8))
print(Solution().searchRange([5,7,7,8,8,10], 6))
print(Solution().searchRange([1], 1))
print(Solution().searchRange([1,2], 0))
print(Solution().searchRange([], 0))