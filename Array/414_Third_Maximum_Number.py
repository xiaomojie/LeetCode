"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlist = [float('-inf'),float('-inf'),float('-inf')]
        for i in nums:
            if i not in maxlist:
                if i > maxlist[0]:
                    maxlist=[i, maxlist[0], maxlist[1]]
                elif i > maxlist[1]:
                    maxlist = [maxlist[0], i, maxlist[1]]
                elif i > maxlist[2]:
                    maxlist = [maxlist[0], maxlist[1], i]
        return maxlist[0] if float('-inf') in maxlist else maxlist[2]

    def thirdMax2(self, nums):
        set_nums = set(nums)
        if len(set_nums) >= 3:
            set_nums.remove(max(set_nums))
            set_nums.remove(max(set_nums))
            return max(set_nums)
        else:
            return max(set_nums)