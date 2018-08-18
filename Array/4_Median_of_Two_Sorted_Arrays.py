"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""

# Time:  O(log(min(m, n)))
# Space: O(1)

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1 + len2) % 2 == 1:
            return self.getKth(nums1, nums2, int((len1 + len2)/2) + 1)
        else:
            return (self.getKth(nums1, nums2, int((len1 + len2)/2)) + self.getKth(nums1, nums2, int((len1 + len2)/2) + 1)) * 0.5

    def getKth(self, A, B, k):
        m, n = len(A), len(B)
        if m > n:
            return self.getKth(B, A, k)
        l = 0
        r = m
        while l < r:
            mid = int((l + r) / 2)
            # print(mid,k, k - 1 - mid,k - 1 - mid )
            if 0 <= k - 1 - mid < n and A[mid] >= B[k - 1 - mid]:
                r = mid
            else:
                l = mid + 1
        A_val, B_val = float("-inf"), float("-inf")
        if l-1 >= 0:
            A_val = A[l-1]
        if k - 1 - l >= 0:
            B_val = B[k-1-l]
        # print(A_val,B_val)
        return max(A_val, B_val)

print(Solution().findMedianSortedArrays([1,3],[2]))