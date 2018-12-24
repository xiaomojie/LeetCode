class Solution:
    def intersection2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set_s = set(nums1)
        set_t = set(nums2)
        res = []
        # for i, x in enumerate(set_s):
        for x in set(set_s):
            if x in set_t:
                res.append(x)
        return res

    def intersection(self, nums1, nums2):
        return list(set(nums1)&set(nums2))

    def intersection3(self, nums1, nums2):
        return list(x for x in set(nums1) if x in set(nums2))


