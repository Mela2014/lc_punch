class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie
        trie = {}
        for word in words:
            curr = trie
            for ch in word:
                curr[ch] = curr.get(ch, {})
                curr = curr[ch]
            curr["end"] = word
        nrow, ncol, rslt, visited = len(board), len(board[0]), set(), set()
        def backtracking(i, j, curr):
            if "end" in curr:
                rslt.add(curr["end"])
            for x, y in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= x < nrow and 0 <= y < ncol and board[x][y] in curr and (x, y) not in visited:
                    visited.add((x, y))
                    backtracking(x, y, curr[board[x][y]])
                    visited.remove((x, y))
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] in trie:
                    visited.add((i, j))
                    backtracking(i, j, trie[board[i][j]])
                    visited.remove((i, j))
        return rslt


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie
        trie = {}
        for word in words:
            curr = trie
            for ch in word:
                curr[ch] = curr.get(ch, {})
                curr = curr[ch]
            curr["end"] = word
        nrow, ncol, rslt = len(board), len(board[0]), set()
        def backtracking(i, j, curr):
            if "end" in curr:
                rslt.add(curr["end"])
            for x, y in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= x < nrow and 0 <= y < ncol and board[x][y] in curr:
                    ch = board[x][y]
                    board[x][y] = ""
                    backtracking(x, y, curr[ch])
                    board[x][y] = ch
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] in trie:
                    ch = board[i][j]
                    board[i][j] = ""
                    backtracking(i, j, trie[ch])
                    board[i][j] = ch
        return rslt

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie
        trie = {}
        for word in words:
            curr = trie
            for ch in word:
                curr[ch] = curr.get(ch, {})
                curr = curr[ch]
            curr["end"] = word
        nrow, ncol, rslt = len(board), len(board[0]), set()
        def backtracking(i, j, parent):
            pch = board[i][j]
            curr = parent[pch]
            board[i][j] = ""
            if "end" in curr:
                rslt.add(curr["end"])
                curr.pop("end")
            for x, y in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= x < nrow and 0 <= y < ncol and board[x][y] in curr:
                    backtracking(x, y, curr)
            board[i][j] = pch
            if not curr:
                parent.pop(pch)
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] in trie:
                    backtracking(i, j, trie)
        return rslt
