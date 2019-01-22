"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 这个题挺好的，归并排序，使用到了链表找中间位，和链表比较大小，合并
# 合并两个函数，两个函数都在很多地方可以用到
class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre = ListNode(0)
        pre.next = head
        slow = fast = head
        while fast and fast.next:
            pre = pre.next
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        return self.merge(self.sortList(head), self.sortList(slow))
        # map() 会根据提供的函数对指定序列做映射。
        # 第一个参数 function 以参数序列中的每一个元素调用 function 函数，
        # 返回包含每次 function 函数返回值的新列表。
        # return self.merge(*map(self.sortList, (head, slow)))


    def merge(self, head1, head2):
        head = cur = ListNode(0)
        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                cur = cur.next
                head1 = head1.next
            else:
                cur.next = head2
                cur = cur.next
                head2 = head2.next
        cur.next = head1 or head2
        return head.next
