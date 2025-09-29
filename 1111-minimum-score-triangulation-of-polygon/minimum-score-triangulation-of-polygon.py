from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0]*n for _ in range(n)]
        
        # Consider sub-polygons of increasing length
        for length in range(2, n):
            for i in range(n-length):
                j = i + length
                dp[i][j] = min(
                    dp[i][k] + dp[k][j] + values[i]*values[k]*values[j]
                    for k in range(i+1, j)
                )
        return dp[0][n-1]
  # Output: 13   explain this 