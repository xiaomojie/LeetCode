"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

class Solution:
    # Time Limit Exceeded
    def findDisappearedNumbers_time_limit(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rlist = []
        for i in range(1,len(nums)+1):
            if i not in nums:
                rlist.append(i)
        return rlist

    # 空间复杂度不是O(1)
    def findDisappearedNumbers2(self, nums):
        return list(set(range(1,len(nums)+1))-set(nums))

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            index = abs(nums[i])-1
            nums[index] = -abs(nums[index])
        return [i+1 for i in range(0, len(nums)) if nums[i]>0]