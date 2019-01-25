
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 先统计长度，然后计算好每一段的长度，例如10，k = 3，则分配为[4,3,3]
    # 然后再循环,在必要的时候掐断
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
        left = count % k
        parts = [avg + 1] * left + [avg] * (k-left)
        res = [0]*len(parts)
        for index, item in enumerate(parts):
            cur = head = ListNode(0)
            head.next = root
            while item:
                cur = cur.next
                item -= 1
            root = cur.next
            cur.next = None
            res[index] = head.next
        return res

