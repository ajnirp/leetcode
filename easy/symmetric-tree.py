# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_mirror(self, n1, n2):
        if n1 is not None and n2 is None:
            return False
        if n2 is not None and n1 is None:
            return False
        if n1 is None and n2 is None:
            return True
        if n1.val != n2.val:
            return False
        return self.is_mirror(n1.left, n2.right) and self.is_mirror(n1.right, n2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.is_mirror(root.left, root.right)