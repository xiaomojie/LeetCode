#-*- coding: utf-8 -*-
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
# Time:  O(n)
# Space: O(1)

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0:
            if nums[i+1] > nums[i]:
                j = i + 1
                while j < len(nums)and nums[j] > nums[i]:
                    j += 1
                tmp = nums[i]
                nums[i] = nums[j-1]
                nums[j-1] = tmp

                # 后面的重排
                nums[i+1:] = sorted(nums[i+1:])
                return
            i -= 1
        nums.sort()


nums = [1, 5, 1]
Solution().nextPermutation(nums)
print(nums)