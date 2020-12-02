class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        def backtracking(i, c, seen):
            if dp[i] > 0 and dp[i] > c + 1 or len(s)-i + c < dp[-1]:
                return
            if i == len(s):
                dp[-1] = max(dp[-1], c)
                return
            for j in range(i+1, len(s)+1):
                if s[i:j] in seen:
                    dp[j-1] = c
                    backtracking(j, c, seen)
                else:
                    dp[j-1] = c+1
                    seen.add(s[i:j])
                    backtracking(j,c+1, seen)
                    seen.remove(s[i:j])
            return
        backtracking(0, 0, set())

        return dp[-1]
