"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.



Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        p = head
        while p:
            if not p.child:
                p = p.next
                continue
            # 有child
            q = p.child
            while q.next:
                q = q.next
            # 到达子链末尾,将末尾与母链下一个节点连接
            q.next = p.next
            if p.next:
                p.next.prev = q
            p.next = p.child
            p.child.prev = p
            p.child = None
        return head

    # # 递归法  存在问题
    # def flatten(self, head):
    #     self.helper(head)
    #     return head
    #
    # def helper(self, head):
    #     cur = pre = head
    #     while cur:
    #         if not cur.child:
    #             pre = cur
    #             cur = cur.next
    #         else:
    #             tmp = cur.next
    #             child = self.helper(cur.child)
    #             cur.next = cur.child
    #             cur.child.pre = cur
    #             cur.child = None
    #             child.next = tmp
    #             if tmp:
    #                 tmp.pre = child
    #             pre = child
    #             cur = tmp
    #     return pre

    # 使用栈
    # def flatten(self, head):
    #     cur, stack = head, []
    #     while cur:
    #         if cur.child:
    #             if cur.next:
    #                 stack.append(cur.next)
    #             cur.next, cur.child.pre, cur.child = cur.child, cur, None
    #         if not cur.next and len(stack):
    #             tmp = stack.pop()
    #             tmp.pre, cur.next = cur, tmp
    #         cur = cur.next
    #     return head

    def flatten1(self, head):
        curr, tempStack = head, []
        while curr:
            if curr.child:
                if curr.next:
                    tempStack.append(curr.next)
                curr.next, curr.child.prev, curr.child = curr.child, curr, None
            if not curr.next and len(tempStack):
                temp = tempStack.pop()
                temp.prev, curr.next = curr, temp
            curr = curr.next
        return head

