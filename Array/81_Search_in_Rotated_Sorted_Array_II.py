"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                left += 1
                right -= 1

            elif (nums[mid] > nums[left] and nums[left] <= target < nums[mid]) or (nums[mid] < nums[left] and not(nums[mid] < target <= nums[right])):
                right = mid - 1
            else:
                left = mid + 1
        return False

nums = [2,5,6,0,0,1,2]
target = 0
# print(Solution().search(nums, target))
nums = [1]
target = 0
print(Solution().search(nums, target))


