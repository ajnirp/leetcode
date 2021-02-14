# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def create_node(self, node, val):
        if node is None:
            node = TreeNode(val)
        else:
            if node.val > val:
                node.left = self.create_node(node.left, val)
            elif node.val < val:
                node.right = self.create_node(node.right, val)
        return node

    def create(self, val):
        self.curr = self.create_node(self.curr, val)

    def bstFromPreorder(self, preorder):
        if len(preorder) == 0:
            return None

        self.curr = None
        for val in preorder:
            self.create(val)

        return self.curr

# def inorder_print(node):
#     if node is None:
#         return
#     inorder_print(node.left)
#     print(node.val)
#     inorder_print(node.right)

# t = Solution().bstFromPreorder([10, 5, 1, 7, 40, 50])
# inorder_print(t)