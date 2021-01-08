# https://leetcode.com/problems/deepest-leaves-sum/
# I solved it by making two passes over the tree, but it can be done in just
# one pass.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def search(self, node, depth, height_):
        if depth == height_:
            if node is not None:
                self.sum += node.val
                return
        if node is None:
            return
        self.search(node.left, depth + 1, height_)
        self.search(node.right, depth + 1, height_)

    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        height_ = self.height(root)
        depth = 1
        self.sum = 0
        self.search(root, depth, height_)
        return self.sum