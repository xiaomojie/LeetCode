"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
import collections


class Solution:
    # 有点慢
    def intersect1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        res = []
        for x in nums1:
            if x in nums2:
               res.append(x)
               nums2.remove(x)
        return res

    def intersect(self, nums1, nums2):
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())


# print(Solution().intersect([3,1,2],[1,1]))
a = [1,2,3,3,4]
b = [1,2,2,3,5]
print(collections.Counter(a))
print(collections.Counter(b))
print(collections.Counter(a) & collections.Counter(b))
print(list((collections.Counter(a) & collections.Counter(b)).elements()))
