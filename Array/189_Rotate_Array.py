"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        nums.reverse()
        # reverse
        for i in range(k%len(nums)//2):
            nums[i], nums[k%len(nums)-1-i] = nums[k%len(nums)-1-i], nums[i]
        # reverse
        for i in range(k%len(nums), (len(nums)+k%len(nums))//2):
            nums[i], nums[len((nums)) - 1 - i + k%len(nums)] = nums[len(nums) - 1 - i + k%len(nums)], nums[i]

    # def rotate1(self, nums, k):
        # reverse(nums)
        # reverse(nums)

nums = [1,2,3,4,5,6]

Solution().rotate(nums, 11)
print(nums)