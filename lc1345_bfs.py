class Solution:
    def minJumps(self, arr: List[int]) -> int:
        valmap, l = collections.defaultdict(list), len(arr)
        if l == 1: return 0
        if arr[0] == arr[l-1]: return 1

        for i, num in enumerate(arr):
            valmap[num].append(i)
        dque, visited, visitednum = collections.deque([(0, 0)]), {0}, set()
        while dque:
            jump, idx = dque.popleft()
            if idx == l-1:
                return jump
            for i in [idx+1, idx-1]:
                if i not in visited and 0<= i < l:
                    dque.append((jump+1, i))
                    visited.add(i)
            if arr[idx] in visitednum: continue
            visitednum.add(arr[idx])
            for i in valmap[arr[idx]]:
                if i not in visited:
                    dque.append((jump+1, i))
                    visited.add(i)
        return len(arr)-1
