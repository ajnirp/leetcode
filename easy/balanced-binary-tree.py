# https://leetcode.com/problems/balanced-binary-tree/

# first pass, store height for each node
# second pass, do inorder traversal (or post or pre, doesn't matter), and check
# that at each node the children's heights differ by no more than 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
