"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""


class Solution:
    # sorting, but O(nlogn)
    def missingNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[0] != 0:
            return 0

        if len(nums) != nums[-1]:
            return len(nums)

        for i in range(len(nums)-1):
            if nums[i] + 1 != nums[i+1]:
                return i+1

    # set
    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        for i in range(len((nums))+1):
            if i not in s:
                return i

    # Gauss' Formula
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums)*(len(nums)+1)//2
        actual = sum(nums)
        return total-actual


nums = [1]
print(Solution().missingNumber(nums))
