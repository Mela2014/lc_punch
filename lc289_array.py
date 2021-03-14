class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrow, ncol = len(board), len(board[0])
        def helper(i, j):
            # -2: change from 1 to 0
            # -1: change from 0 to 1
            cl = 0
            for x, y in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j -1), (i, j+1),(i+1, j-1), (i+1, j), (i+1, j+1)]:
                if x < 0 or x >= nrow or y < 0 or y >= ncol:
                    continue
                cl += 1 if board[x][y] in (1, -2) else 0
            return cl

        for i in range(nrow):
            for j in range(ncol):
                cl = helper(i, j)
                if board[i][j] == 1 and (cl < 2 or cl > 3):
                    board[i][j] = -2
                if board[i][j] == 0 and cl == 3:
                    board[i][j] = -1
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] < 0:
                    board[i][j] += 2
