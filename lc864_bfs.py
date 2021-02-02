class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        k, nrow, ncol = 0, len(grid), len(grid[0])
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == "@": start = (i, j)
                elif grid[i][j] in string.ascii_lowercase: k += 1
        dque, visited= collections.deque([(0, start[0], start[1], "")]), {}
        while dque:
            step, x, y, getk = dque.popleft()
            if len(getk) == k:
                return step
            for dx, dy in [(x+1,y), (x, y+1), (x,y-1), (x-1, y)]:
                newk = getk
                if 0 <= dx < nrow and 0 <= dy < ncol and grid[dx][dy] !="#":
                    tc = grid[dx][dy]
                    if tc in string.ascii_uppercase and tc.lower() not in newk:
                        continue
                    if tc in string.ascii_lowercase and tc not in newk:
                        newk += tc
                    if (dx, dy, newk) not in visited:
                        visited.add((dx, dy, newk))
                        dque.append((step+1, dx, dy, newk))
        return -1


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        k, nrow, ncol = 0, len(grid), len(grid[0])
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == "@": start = (i, j)
                elif grid[i][j] in string.ascii_lowercase: k += 1
        dque, visited= collections.deque([(0, start[0], start[1], 0)]), {}
        while dque:
            step, x, y, getk = dque.popleft()
            if getk == 2**k-1:
                return step
            for dx, dy in [(x+1,y), (x, y+1), (x,y-1), (x-1, y)]:
                newk = getk
                if 0 <= dx < nrow and 0 <= dy < ncol and grid[dx][dy] !="#":
                    tc = grid[dx][dy]
                    if tc in string.ascii_uppercase and (1 << ord(tc.lower())-ord('a'))&newk == 0:
                        continue
                    if tc in string.ascii_lowercase and (1 << (ord(tc)-ord('a')))&newk == 0:
                        newk |= 1 << (ord(tc)-ord('a'))
                    if (dx, dy, newk) not in visited:
                        visited.add((dx, dy, newk))
                        dque.append((step+1, dx, dy, newk))
        return -1
