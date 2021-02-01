# https://leetcode.com/problems/binary-tree-level-order-traversal-ii

from collections import deque

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return []
        q = deque([[root]])
        result = deque()
        while len(q) > 0:
            curr_level = q.popleft()
            next_level = []
            for node in curr_level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            if len(next_level) > 0:
                q.append(next_level)
            if len(curr_level) > 0:
                result.appendleft([n.val for n in curr_level])
        return list(result)