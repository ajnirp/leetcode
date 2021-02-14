# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, node, path):
        if not (node.left or node.right):
            self.result.append(path + [node.val])
        if node.left:
            self.helper(node.left, path + [node.val])
        if node.right:
            self.helper(node.right, path + [node.val])

    def format_path(self, path):
        return '->'.join(map(str, path))

    def binaryTreePaths(self, root):
        if root is None:
            return []
        self.result = []
        self.helper(root, [])
        return [self.format_path(path) for path in self.result]

t = TreeNode(1,
         TreeNode(2,
                  None,
                  TreeNode(5)),
         TreeNode(3))


print(Solution().binaryTreePaths(t))