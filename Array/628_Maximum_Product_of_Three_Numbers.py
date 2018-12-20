"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""


class Solution:
    def maximumProduc1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # 可能有负数存在
        return max(nums[-1] * nums[-2] * nums[-3], nums[-1] * nums[0] * nums[1])

    def maximumProduct(self, nums):
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        for i in range(len(nums)):
            if nums[i] > max1:
                max1, max2, max3 = nums[i], max1, max2

            elif nums[i] > max2:
                max2, max3 = nums[i], max2
            elif nums[i] > max3:
                max3 = nums[i]

            if nums[i] < min1:
                min1, min2 = nums[i], min1
            elif nums[i] < min2:
                min2 = nums[i]
        return max(max1*max2*max3, max1*min1*min2)

print(Solution().maximumProduc1([1,2,3,4]))