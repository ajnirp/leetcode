# https://leetcode.com/problems/maximal-square/submissions/

# for each cell, go one up and one left, and check the maximal square length at
# that length, and then use that number as an iteration upper bound to find the
# maximal square length at that current cell

class Solution:
    def bounds(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def helper(self, r, c):
        if not self.bounds(r, c):
            return 0

        if self.memo[r][c] < 0:
            if self.matrix[r][c] == '0':
                self.memo[r][c] = 0
            else:
                recur = self.helper(r-1, c-1)
                vert = 0
                for i in range(recur+1):
                    rr, cc = r-i, c
                    if self.bounds(rr, cc) and self.matrix[rr][cc] == '1':
                        vert = i
                    else:
                        break
                hori = 0
                for i in range(recur+1):
                    rr, cc = r, c-i
                    if self.bounds(rr, cc) and self.matrix[rr][cc] == '1':
                        hori = i
                    else:
                        break
                self.memo[r][c] = 1 + min(vert, hori)

        self.result = max(self.result, self.memo[r][c])
        return self.memo[r][c]

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.matrix = matrix
        self.result = 0
        self.memo = [[-1 for _ in range(self.cols)] for _ in range(self.rows)]

        if self.rows == 0 or self.cols == 0:
            return 0

        for r in range(self.rows):
            for c in range(self.cols):
                self.helper(r, c)

        return self.result * self.result
