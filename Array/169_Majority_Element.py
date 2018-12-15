"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for item in nums:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
            if d[item] > len(nums) // 2:
                return item

    def majorityElement2(self, nums):
        return sorted(nums)[len(nums) // 2]
    

nums = [1,3,3,4,5,5,5,5]
print(Solution().majorityElement2(nums))