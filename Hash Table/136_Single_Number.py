"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""


class Solution:
    # 超时
    def singleNumber5(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in set(nums):
            if nums.count(i) == 1:
                return i
        return None

    # a⊕0=a
    # a⊕a=0
    # a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
    # time: O(n)
    # space: O(1)
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a

    # time: O(n^2), iterate through \text{nums}nums, taking O(n)time. We search the whole list to find whether
    # there is duplicate number, taking O(n) time
    # space: O(n)
    def singleNumber(self, nums):
        res = []
        for i in nums:
            if i not in res:
                res.append(i)
            else:
                res.pop(i)
        return res.pop()

    # time: O(n), Time complexity of hash table(dictionary in python) operation pop is O(1).
    # space: O(n)
    def singleNumber(self, nums):
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

    # 2∗(a+b+c)−(a+a+b+b+c) = c
    # time: O(n)
    # space: O(n)
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)



print(Solution().singleNumber([2,2,1]))
print(Solution().singleNumber([4,1,2,1,2]))