class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        pdque, adque = collections.deque(), collections.deque()
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            pdque.append((i, 0))
            adque.append((i, m-1))
        for j in range(m):
            pdque.append((0, j))
            adque.append((n-1, j))
        def bfs(queue):
            visited = set()
            while queue:
                x, y  = queue.popleft()
                if (x, y) in visited:
                    continue
                visited.add((x,y))
                for nx, ny  in [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]:
                    if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] >= matrix[x][y] and (nx, ny) not in visited:
                        queue.append((nx, ny))
            return visited
        return bfs(pdque) & bfs(adque)
