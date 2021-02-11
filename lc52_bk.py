class Solution:
    def totalNQueens(self, n: int) -> int:
        self.rslt, visited = 0, set()
        def backtracking(i):
            if i == n:
                self.rslt += 1
            else:
                for j in range(n):
                    if (2, j) not in visited and (3, j-i) not in visited and (4, j+i) not in visited:
                        visited.add((2, j))
                        visited.add((3, j-i))
                        visited.add((4, j+i))
                        backtracking(i+1)
                        visited.remove((2, j))
                        visited.remove((3, j-i))
                        visited.remove((4, j+i))
        backtracking(0)
        return self.rslt
