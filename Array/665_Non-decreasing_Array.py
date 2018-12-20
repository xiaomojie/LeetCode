"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""


class Solution:
    def checkPossibility1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        one, two = nums[:], nums[:]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                one[i] = one[i+1]
                two[i+1] = two[i]
                break
        return one == sorted(one) or two == sorted(two)


    def checkPossibility(self, nums):
        count = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
                if i-1 < 0 or nums[i-1] < nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
        return count <= 1



print(Solution().checkPossibility([4,2,3]))
print(Solution().checkPossibility([4,2,1]))
print(Solution().checkPossibility([4,2,7,8,7]))
