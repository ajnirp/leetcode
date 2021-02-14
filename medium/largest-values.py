# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        curr_level = [root]
        result = []
        while len(curr_level) > 0:
            next_level = []
            max_val = curr_level[0].val
            for node in curr_level:
                max_val = max(max_val, node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append(max_val)
            curr_level = next_level
        return result