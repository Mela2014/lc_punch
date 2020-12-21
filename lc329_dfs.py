class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        @lru_cache(None)
        def dfs(i, j):
            temp = 1
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if i+x >= 0 and i+x < len(matrix) and j+y >= 0 and j+y < len(matrix[0]) and matrix[i+x][j+y] > matrix[i][j]:
                    temp = max(temp, dfs(i+x, j+y)+1)
            return temp
        rslt = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                rslt = max(rslt, dfs(i, j))
        return rslt
