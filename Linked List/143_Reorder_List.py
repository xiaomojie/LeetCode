"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 思路，先找到中间，把链表分成两半，再把后一半翻转，然后在合并两个链表
class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        list1, list2 = self.splitList(head)
        list2 = self.reverseList(list2)
        return self.mergeLists(list1, list2)

    def splitList(self, head):
        pre = ListNode(0)
        pre.next = slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            pre = pre.next
        pre.next = None
        return head, slow

    # 这里合并不是比较大小合并了，而是交叉合并
    def mergeLists(self, list1, list2):
        cur = ListNode(0)
        while list1 and list2:
            cur.next = list1
            cur = cur.next
            cur.next = list2
            cur = cur.next
            list1, list2 = list1.next, list2.next
        cur.next = list1 or list2

    # 迭代翻转
    def reverseList(self, head):
        pre = None
        while head:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
        return pre