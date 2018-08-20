"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

"""
# Time:  O(n)
# Space: O(1)

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        currentMax = 0
        lastMax = 0
        for i in range(len(nums)-1):
            if lastMax < i:
                return False
            currentMax = max(currentMax, nums[i] + i)
            if i == lastMax:
                lastMax = currentMax
        if currentMax >= len(nums) - 1:
            return True
        else:
            return False

print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump( [3,2,1,0,4]))
print(Solution().canJump( [1,0,1,0]))
print(Solution().canJump( [0,1,0]))