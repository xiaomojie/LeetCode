"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which
is more subtle.
"""


# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxSum = current = nums[0]
        for n in nums[1:]:
            current = max(current + n, n)
            maxSum = max(maxSum, current)
        return maxSum

