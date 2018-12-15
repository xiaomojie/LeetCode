"""

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
# 由中序遍历和后序遍历确定树结构
# 后续遍历的最后一个节点为根节点，但是对后续数组从后往前遍历时，先遇到的时右子树


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            index = inorder.index(postorder.pop())
            root = TreeNode(inorder[index])

            root.right = self.buildTree(inorder[index+1:], postorder)
            root.left = self.buildTree(inorder[:index], postorder)

            return root


inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(Solution().buildTree(inorder, postorder))
