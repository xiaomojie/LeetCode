"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 这个思想挺巧妙的，设置a和b，让a先走完第一条链再从头开始走第二条链，
    # b先走第二条再走第一条，则第第二轮走的时候必定会在交点相遇
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        a = headA
        b = headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

