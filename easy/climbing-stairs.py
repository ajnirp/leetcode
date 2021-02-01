# https://leetcode.com/problems/climbing-stairs/

# archetypal DP-style solution
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0 for _ in range(n+1)]
        memo[0] = 1
        memo[1] = 1
        def helper(k, memo):
            if memo[k] > 0:
                return memo[k]
            res1 = helper(k-1, memo)
            res2 = helper(k-2, memo)
            memo[k-1] = res1
            memo[k-2] = res2
            return res1 + res2
        return helper(n, memo)

# most optimal solution, barring the analytical one
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a+b
        return a