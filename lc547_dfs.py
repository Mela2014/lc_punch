class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(j)
        visited, rslt= [0]*len(isConnected), 0
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                rslt += 1
        return rslt
