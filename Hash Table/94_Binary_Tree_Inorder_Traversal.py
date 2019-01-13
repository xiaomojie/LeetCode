"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归解法BFS
        # time: O(n)
        # space:
        res = []
        if root is None:
            return res
        res.extend(self.inorderTraversal(root.left))
        res.extend([root.val])
        res.extend(self.inorderTraversal(root.right))
        return res

    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            root = stack.pop()
            res.append(root.val)
            root = root.right