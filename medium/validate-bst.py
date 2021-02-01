# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# inorder traversal followed by sortedness check
# uses linear extra space
class Solution:
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        self.inorder_output.append(node.val)
        self.inorder(node.right)

    def is_sorted(self, arr):
        return all(arr[i] < arr[i+1] for i in range(len(arr)-1))

    def isValidBST(self, root: TreeNode) -> bool:
        self.inorder_output = []
        self.inorder(root)
        return self.is_sorted(self.inorder_output)

# no extra space used, same time complexity
class Solution:
    def helper(self, node, min_, max_):
        if node is None:
            return True
        if not (min_ < node.val < max_):
            return False
        return self.helper(node.left, min_, node.val) and self.helper(node.right, node.val, max_)

    def isValidBST(self, root):
        return self.helper(root, -(1 << 31) - 1, 1 << 31)