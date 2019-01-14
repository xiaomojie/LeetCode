"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


from collections import Counter
class Solution(object):
    def topKFrequent1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        temp = sorted(Counter(nums).items(), key=lambda d: d[1],  reverse=True)
        return [x[0] for x in temp[0:k]]

    def topKFrequent(self, nums, k):
        # python 2是没问题的，python 3下面这个会报错
        # return zip(*Counter(nums).most_common(k))[0]

        return list(zip(*Counter(nums).most_common(k)))[0]

print(Solution().topKFrequent([1,1,1,2,2,3], 2))
