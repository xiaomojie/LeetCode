"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 由于python中int没有最大值，所以可以先计算和，然后再来构造链表
    # 这种方法貌似有点取巧的感觉
    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum1 = sum2 = 0
        while l1:
            sum1 = sum1*10 + l1.val
            l1 = l1.next
        while l2:
            sum2 = sum2*10 + l2.val
            l2 = l2.next
        sum = sum1 + sum2
        head = ListNode(0)
        if not sum:
            return head
        while sum:
            head.next, head.next.next = ListNode(sum % 10), head.next
            sum //= 10
        return head.next

    # 使用栈
    def addTwoNumbers(self, l1, l2):
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        sum = 0
        head = ListNode(0)
        while len(stack1) or len(stack2) or sum:
            if len(stack1):
                sum += stack1.pop()
            if len(stack2):
                sum += stack2.pop()
            node = ListNode(sum % 10)
            node.next = head.next
            head.next = node
            sum //= 10
        return head.next



