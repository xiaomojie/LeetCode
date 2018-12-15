"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

    # Time Limit Exceeded
    # def containsDuplicate1(self, nums):
    #     for i in range(len(nums)):
    #         if nums[i] in nums[:i]:
    #             return True
    #     return False

    def containsDuplicate2(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return  True
        return False

nums = [1,2,3,1]
print(Solution().containsDuplicate(nums))
# print(Solution().containsDuplicate1(nums))
print(Solution().containsDuplicate2(nums))