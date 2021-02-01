# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, depth):
        if node is None:
            return
        self.max_depth = max(self.max_depth, depth)
        self.helper(node.left, depth+1)
        self.helper(node.right, depth+1)

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.max_depth = 1
        self.helper(root, 1)
        return self.max_depth