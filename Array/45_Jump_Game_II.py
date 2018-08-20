# -*- coding:utf-8 -*-
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""
# Time:  O(n)
# Space: O(1)


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_max_reach = 0
        current_max_reach = 0
        count = 0
        for i in range(len(nums)-1):
            current_max_reach = max(current_max_reach, i + nums[i])
            if i == last_max_reach:  # 如果当前已经到达了上一次能够到的最大位置，这时必须要增加一步
                count += 1
                last_max_reach = current_max_reach
        return count

    def jump2(self, nums):
        if len(nums) < 2:
            return 0

        level = 0
        currentMax = 0
        i = 0
        next_max = 0
        while currentMax - i + 1 > 0:
            level += 1
            while i <= currentMax:
                next_max = max(next_max, nums[i] + i)
                if next_max >= len(nums) - 1:
                    return level
                i += 1
            currentMax = next_max

        return 0

print(Solution().jump2([2,2,2,1,1]))


