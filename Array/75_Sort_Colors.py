"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        left = 0
        right = len(nums) - 1
        while i <= right:
            if nums[i] == 0:
                if left != i:
                    nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1

            elif nums[i] == 2:
                if right != i:
                    nums[i], nums[right] = nums[right], nums[i]
                right -= 1

            else:
                i += 1
            print(nums, left, right, i)


nums = [2,0,2,1,1,0]
Solution().sortColors(nums)
print(nums)


