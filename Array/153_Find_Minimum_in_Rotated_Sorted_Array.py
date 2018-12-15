"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""


class Solution:
    # O(n)
    def findMin1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        min = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < min:
                return nums[i]
        return min

    # binary search O(log n)
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or nums[-1] > nums[0]:
            return nums[0]

        left = 0
        right = len(nums)-1

        start = nums[0]

        while left < right:
            mid = (left + right)//2
            if nums[mid] >= start:
                left = mid+1
            else:
                right = mid
        return nums[left]
nums = [2,1]
print(Solution().findMin(nums))
