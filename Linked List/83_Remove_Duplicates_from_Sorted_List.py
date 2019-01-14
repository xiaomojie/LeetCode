"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 迭代
    def deleteDuplicates1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        val = [head.val]
        prev = head
        cur = head.next
        while cur:
            if cur.val in val:
                prev.next = cur.next

            else:
                val.append(cur.val)
                prev = prev.next
            cur = cur.next
        return head

    # 迭代
    def deleteDuplicates1_1(self, head):
        if not head:
            return head
        prev = head
        cur = head.next
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return head

    # 迭代
    def deleteDuplicates2(self, head):
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

    # 递归
    def deleteDuplicates(self, head):
        if head and head.next and head.val == head.next.val:
            head = self.deleteDuplicates(head.next)
        elif head and head.next:
            head.next = self.deleteDuplicates(head.next)
        return head