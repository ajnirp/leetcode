# https://leetcode.com/problems/number-of-provinces/

# idea: do dfs for each node. when doing dfs, mark it as seen in a set.
# the set is shared by the entire graph. right before starting a search in the
# driver method, check if the node was seen before. if not, it's the first node
# to be seen in a new component, so increment num_components.

def make_nbr_list(adj_matrix):
    result = {}
    for i in range(len(adj_matrix)):
        result[i] = []
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] == 1:
                result[i].append(j)
    return result

def dfs(node, nbrs, seen):
    if node in seen:
        return
    seen.add(node)
    for nbr in nbrs[node]:
        dfs(nbr, nbrs, seen)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        nbrs = make_nbr_list(isConnected)
        seen = set()
        result = 0
        for node in nbrs:
            if node not in seen:
                result += 1
            dfs(node, nbrs, seen)
        return result