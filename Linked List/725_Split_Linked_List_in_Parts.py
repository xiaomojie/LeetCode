# 先统计长度，然后计算好每一段的长度，例如10，k = 3，则分配为[4,3,3]
# 然后外层循环为range(3), 内层循环为[4,3,3],在必要的时候掐断
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        cur = root
        count = 0
        while cur:
            cur, count = cur.next, count+1
        avg = count//k
        leave = count % k
        parts = [avg + 1] * leave + [avg] * (k-leave)
        res = []
        cur = root
        for i in parts:
            while i and cur:
                i -= 1