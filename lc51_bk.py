class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rslt, visited= [], set()
        def backtracking(i, curr):
            if len(curr) == n:
                rslt.append(curr)
            else:
                for j in range(n):
                    if (2, j) not in visited and (3, j-i) not in visited and (4, j+i) not in visited:
                        visited.add((2, j))
                        visited.add((3, j-i))
                        visited.add((4, j+i))
                        backtracking(i+1, curr + ["."*j+"Q"+"."*(n-j-1)] )
                        visited.remove((2, j))
                        visited.remove((3, j-i))
                        visited.remove((4, j+i))
        backtracking(0, [])
        return rslt
