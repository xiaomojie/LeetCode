"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
思路:首先先设置一个fast一个slow，当fast和slow相遇了之后，c再从head出发，
c一定会和slow在环的入口相遇，并且是当c第一次到达入口时相遇

证明：head到环入口距离为H，环的长度为L，当slow走了H+D时与fast相遇，D为slow在环中走的距离，此时
fast走了H+D+nL,因为fast的速度是slow的两倍，则fast走的距离也是slow的两倍：2(H+D) = H+D+nL ==> H=nL-D,
此时c从head出发，到环入口走H = NL-D，slow再走H也到达入口，此时slow走的距离为H+D+H = 2NL-2D+D = 2NL-D
,可见slow正好比c多走NL，所以必定会在环入口相遇

证明fast和slow必定会相遇：fast和slow的速度差为v，在环中对于任意的距离NL+X，必定会存在T=(NL+X)/V有解，
即T有解

"""
class Solution(object):
    # 两种方法差不多，只是开始节点不同，第一种更好一些
    def detectCycle1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            head = head.next
            slow = slow.next
        return head

    def detectCycle(self, head):
        try:
            fast = head.next
            slow = head
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
        except:
            return None
        # since fast starts at head.next, we need to move slow one step forward
        slow = slow.next
        while head is not slow:
            slow = slow.next
            head = head.next
        return head