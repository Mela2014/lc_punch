class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        dque, visited, n = collections.deque([(0, 0)]), {0}, len(board)
        while dque:
            step, t = dque.popleft()
            dx = n-t//n-1
            dy = t%n if t//n%2 == 0 else n-t%n-1
            if board[dx][dy] > 0:
                t = board[dx][dy]-1
            if t+1 == n*n: return step
            for s in range(1, 7):
                curr = t+s
                if curr not in visited and 0 <= curr < n*n:
                    dque.append((step+1, curr))
                    visited.add(curr)
        return -1
