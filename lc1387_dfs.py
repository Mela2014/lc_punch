# dfs + memoization
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1:1}
        def dfs(i):
            if i in memo:
                return memo[i]
            elif i%2 == 0:
                memo[i] = dfs(i//2) + 1
            else:
                memo[i] = dfs(3*i + 1) + 1
            return memo[i]
        rslt = []
        for i in range(lo, hi+1):
            rslt.append((i, dfs(i)))
        rslt.sort(key=lambda x: x[1])
        return rslt[k-1][0]


# slow bfs
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        queue = collections.deque()
        for i in range(lo, hi+1):
            queue.append((i, 0, i))
        rslt = []
        while queue:
            ori, curr_power, curr = queue.popleft()
            if curr == 1:
                rslt.append(ori)
            elif curr %2 == 0:
                queue.append((ori, curr_power+1, curr//2))
            else:
                queue.append((ori, curr_power+1, curr*3 + 1))
            if len(rslt) == k:
                break
        return rslt[-1]
