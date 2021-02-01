# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# quite similar to finding max depth of a binary tree: max-depth.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, path):
        if node is None:
            return
        if node.left is None and node.right is None:
            self.result += int(''.join(path + [str(node.val)]))
            return
        self.helper(node.left, path + [str(node.val)])
        self.helper(node.right, path + [str(node.val)])

    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.result = 0
        self.helper(root, [])
        return self.result