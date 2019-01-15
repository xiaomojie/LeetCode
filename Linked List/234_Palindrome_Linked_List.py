"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 对列表的一半进行翻转，然后将翻转之后的和未翻转的进行比较
    # 但是会改变原来的结构
    def isPalindrome1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pre = None
        fast = slow = head
        while fast and fast.next:
            cur = slow
            fast = fast.next.next
            slow = slow.next
            cur.next = pre
            pre = cur
        if fast:
            slow = slow.next
        while pre and pre.val == slow.val:
            pre = pre.next
            slow = slow.next
        return not pre

    # 也和上面一样，就是在比较的时候再将翻转复原
    def isPalindrome(self, head):
        pre = None
        fast = slow = head
        while fast and fast.next:
            cur = slow
            fast = fast.next.next
            slow = slow.next
            cur.next = pre
            pre = cur
        cur = slow
        if fast:
            slow = slow.next
        res = True
        while pre:
            if pre.val != slow.val:
                res = False
            temp = pre
            pre = pre.next
            temp.next = cur
            cur = temp

            slow = slow.next

        return res
a = 1
b = 2
c = 3
a,b,c=b,c,a
print(a,b,c)