# https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, val):
        if node is None:
            return

        if node.val != val:
            self.result = False
            return

        self.helper(node.left, val)
        self.helper(node.right, val)

    def isUnivalTree(self, root: TreeNode) -> bool:
        self.result = True

        if root is not None:
            self.helper(root, root.val)

        return self.result