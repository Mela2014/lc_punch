class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        start, nrow, ncol = 0, len(mat), len(mat[0])
        for i in range(nrow):
            for j in range(ncol):
                start |= mat[i][j]<< (i*ncol+j)
        dque, visited, step = collections.deque([start]), {start}, 0
        while dque:
            size = len(dque)
            for _ in range(size):
                curr = dque.popleft()
                if curr == 0: return step
                for i in range(nrow):
                    for j in range(ncol):
                        temp = curr
                        for di, dj in [(i, j), (i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                            if 0 <= di < nrow and 0 <= dj < ncol:
                                temp ^= 1 <<(di*ncol + dj)
                        if temp not in visited:
                            visited.add(temp)
                            dque.append(temp)
            step += 1
        return -1 
