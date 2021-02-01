# https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_leaf(self, node):
        return node.left is None and node.right is None

    def helper(self, node, sum_so_far, targetSum):
        sum_so_far += node.val
        if self.is_leaf(node):
            return sum_so_far == targetSum
        else:
            left_recur = False
            if node.left is not None:
                left_recur = self.helper(node.left, sum_so_far, targetSum)
            right_recur = False
            if node.right is not None:
                right_recur = self.helper(node.right, sum_so_far, targetSum)
            return left_recur or right_recur

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return targetSum == 0
        return self.helper(root, 0, targetSum)