# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal_rec(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal(self, root):
        res = []
        if not root:
            return res
        stack = []
        p = root

        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                res.append(p.val)
                p = p.right
        return res
