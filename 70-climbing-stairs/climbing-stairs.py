class Solution:
    def climbStairs(self, n: int) -> int:
        def combo(n, dp):
            if n == 1:
                return 1
            if n == 0:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] = combo(n-1,dp) + combo(n-2, dp)
            return dp[n]
        dp = [-1] * (n + 1)
        return combo(n, dp)