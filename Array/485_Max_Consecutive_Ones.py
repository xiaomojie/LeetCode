"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

class Solution:
    def findMaxConsecutiveOnes1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        maxlen = 0
        while i < len(nums):
            if nums[i] != 1:
                i += 1
                continue
            else:
                curr_len = 1
                i += 1
                while i < len(nums) and nums[i] == 1:
                    curr_len += 1
                    i+=1
                maxlen = max(maxlen, curr_len)
        return maxlen

    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                ans = max(cnt,ans)
            else:
                cnt = 0
        return ans