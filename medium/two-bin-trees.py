# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        return self.merge(self.inorder(root1), self.inorder(root2))

    # return inorder traversal of a binary tree as a list
    def inorder(self, root):
        def helper(node, result):
            if node is None:
                return
            helper(node.left, result)
            result.append(node.val)
            helper(node.right, result)
        result = []
        helper(root, result)
        return result

    # merge two sorted lists
    def merge(self, l1, l2):
        i, j = 0, 0
        result = []
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                result.append(l1[i])
                i += 1
            else:
                result.append(l2[j])
                j += 1
        while i < len(l1):
            result.append(l1[i])
            i += 1
        while j < len(l2):
            result.append(l2[j])
            j += 1
        return result