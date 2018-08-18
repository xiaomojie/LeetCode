"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to
target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

# Time:  O(n^2)
# Space: O(1)


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        closest = nums[0] + nums[1] + nums[len(nums)-1]
        i = 0
        while i < len(nums)-2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if abs(closest-target) > abs(sum - target):
                    closest = sum
                if sum > target:
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    return closest
                    # k -= 1
                    # j += 1
            i += 1
        return closest


print(Solution().threeSumClosest([-1,2,1,-4], 2))


