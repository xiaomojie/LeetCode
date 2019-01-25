"""
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # solution 1
    def swapPairs1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = pre = ListNode(0)
        pre.next = head
        cur = head
        while cur and cur.next:
            next = cur.next
            cur.next = next.next
            next.next = cur
            pre.next = next
            pre = cur
            cur = cur.next
        return p.next

    def swapPairs(self, head):
        if not head or not head.next:
            return head
        n = head.next
        head.next = self.swapPairs(head.next.next)
        n.next = head
        return n