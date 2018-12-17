"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = sorted(nums)
        begin = len(nums)-1
        end = 0
        for i in range(len(nums)):
            if sort_nums[i] != nums[i]:
                begin = min(begin, i)
                end = max(end, i)
        return end - begin + 1 if end > begin else 0

    def findUnsortedSubarray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, sorts = len(nums), sorted(nums)
        if nums == sorts: return 0
        l, r = min(i for i in range(n) if nums[i] != sorts[i]), max(i for i in range(n) if nums[i] != sorts[i])
        return r - l + 1

    def findUnsortedSubarray1(self, nums):
        begin = -1
        end = -2
        max_nums = nums[0]
        min_nums = nums[len(nums)-1]
        for i in range(len(nums)):
            max_nums = max(max_nums, nums[i])
            min_nums = min(min_nums, nums[len(nums)-1-i])
            if nums[i] < max_nums:
                end = i
            if nums[len(nums)-1-i] > min_nums:
                begin = len(nums)-1-i
        return end - begin + 1



nums =  [2, 6, 4, 8, 10, 9, 15]
print(Solution().findUnsortedSubarray(nums))