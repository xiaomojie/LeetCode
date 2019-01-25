"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = pre = ListNode(0)
        pre.next = head
        cur = head
        while cur and cur.next:
            if cur.val != cur.next.val:
                pre = pre.next
                cur = cur.next
                continue
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
            pre.next = cur

        return p.next
