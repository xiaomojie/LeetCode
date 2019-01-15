"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 递归
    def removeElements1(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        head.next = self.removeElements(head.next, val)
        return head if head.val != val else head.next

    # 迭代
    def removeElements2(self, head, val):
        res = prev = ListNode(0)
        prev.next = cur = head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return res.next

    def removeElements(self, head, val):
        _head = ListNode(float("-inf"))
        _head.next = head

        curr = _head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return _head.next


