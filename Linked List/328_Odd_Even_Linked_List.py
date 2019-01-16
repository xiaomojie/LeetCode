"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        head_odd = odd = ListNode(0)
        head_even = even = ListNode(0)
        cur = head
        while cur and cur.next:
            odd.next = cur
            odd = odd.next
            even.next = cur.next
            even = even.next
            cur = cur.next.next
        if cur:
            odd.next = cur
            odd = odd.next
        even.next = None
        odd.next = head_even.next
        return head_odd.next

    # 上面版本的简化版
    def oddEvenList(self, head):
        head_odd = odd = ListNode(0)
        head_even = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = head_even.next
        return head_odd.next


