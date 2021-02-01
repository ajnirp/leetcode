# https://leetcode.com/problems/triangle/

# # Improvements:
# # 1. use 2d array over map
# # 2. user 1d array only. rewrite it with minimum path sums for each row as you go down the triangle

# # naivest - map that remembers min path sum for all cells
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         def helper(triangle, row, col, memo):
#             if row == 0:
#                 return triangle[0][0]
#             if (row, col) not in memo:
#                 if col == 0:
#                     memo[(row, col)] = triangle[row][col] + helper(triangle, row-1, 0, memo)
#                 elif col == len(triangle[row])-1:
#                     memo[(row, col)] = triangle[row][col] + helper(triangle, row-1, len(triangle[row-1])-1, memo)
#                 else:
#                     cand_1 = triangle[row][col] + helper(triangle, row-1, col-1, memo)
#                     cand_2 = triangle[row][col] + helper(triangle, row-1, col, memo)
#                     memo[(row, col)] = min(cand_1, cand_2)
#             return memo[(row, col)]
#         memo = {}
#         return min(helper(triangle, len(triangle)-1, c, memo) for c in range(len(triangle[-1])))

# best - 1d array
class Solution:
    def minimumTotal(self, triangle):
        if len(triangle) == 0:
            return 0
        memo = [1e10 for _ in triangle[-1]]
        memo[0] = triangle[0][0]
        for row in range(1, len(triangle)):
            new_memo = [m for m in memo]
            for col in range(row+1):
                if col == 0:
                    new_memo[col] = memo[col]
                elif col == row:
                    new_memo[col] = memo[col-1]
                else:
                    new_memo[col] = min(memo[col], memo[col-1])
                new_memo[col] += triangle[row][col]
            memo = [m for m in new_memo]
        return min(memo)

t = [[-1],[3,2],[1,-2,-1]]
print(Solution().minimumTotal(t))