"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""

# Time:  O(logn)
# Space: O(1)


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l <= r:
            m = int((l + r)/2)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return l

    def searchInsert2(self, nums, target):
        if len(nums) == 0:
            return 0
        N = len(nums)
        mid = int(N / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.searchInsert2(nums[:mid], target)
        else:
            res = self.searchInsert2(nums[mid+1:], target)
            return res + mid + 1

print(Solution().searchInsert([1, 3, 5, 6], 4))
print(Solution().searchInsert2([1, 3, 5, 6], 4))


