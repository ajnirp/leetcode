# https://leetcode.com/problems/average-of-levels-in-binary-tree/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q = deque([[root]])
        result = []
        while len(q) > 0:
            curr_level = q.popleft()
            result.append(sum(n.val for n in curr_level) / len(curr_level))
            new_level = []
            for n in curr_level:
                if n.left:
                    new_level.append(n.left)
                if n.right:
                    new_level.append(n.right)
            if len(new_level) > 0:
                q.append(new_level)
        return result