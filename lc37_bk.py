class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        memo = collections.defaultdict(set)
        # store curr board:
        for i, l in enumerate(board):
            for j, t in enumerate(l):
                if t !=".":
                    memo[(i, -1)].add(t)
                    memo[(-1, j)].add(t)
                    memo[(i//3, j//3)].add(t)
        def backtracking(i, j):
            if i == 9:
                return True
            if board[i][j] == ".":
                for t in "123456789":
                    if t not in memo[(i,-1)] and t not in memo[(-1, j)] and t not in memo[(i//3, j//3)]:
                        board[i][j] = t
                        memo[(i, -1)].add(t)
                        memo[(-1, j)].add(t)
                        memo[(i//3, j//3)].add(t)
                        if j < 8 and backtracking(i, j+1):
                            return True
                        if j == 8 and backtracking(i+1, 0):
                            return True
                        board[i][j] = "."
                        memo[(i, -1)].remove(t)
                        memo[(-1, j)].remove(t)
                        memo[(i//3, j//3)].remove(t)
                return False
            else:
                if j < 8 :
                    return backtracking(i, j+1)
                else:
                    return backtracking(i+1, 0)
        backtracking(0, 0)
        return board
