class Solution:
    def getNarcissisticNumbers(self, n):
        ans = []
        def dfs(i: int, num: int, s: int):
            if i == n and s == num: ans.append(num)
            if i == n: return
            if s > (num + 1) * (10 ** (n - i)) - 1: return
            start = 1 if n > 1 and i == 0 else 0
            for p in range(start, 10):
                dfs(i + 1, num * 10 + p, s + p ** n)
        dfs(0, 0, 0)
        return ans