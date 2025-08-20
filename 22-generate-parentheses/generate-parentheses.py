class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
         ans = []
         self.solve(n, n, "", ans)
         return ans

    def solve(self, n, c, temp, ans):
        if n == 0 and c == 0:
            ans.append(temp)
            return
        if n > 0:
            self.solve(n - 1, c, temp + "(", ans)
        if n < c:
            self.solve(n, c - 1, temp + ")", ans)