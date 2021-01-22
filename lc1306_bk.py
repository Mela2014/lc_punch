class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        self.rslt, larr = False, len(arr)
        def backtracking(idx):
            if arr[idx] == 0:
                self.rslt = True
                return
            if idx in seen:
                return
            seen.add(idx)
            if idx + arr[idx] < larr:
                backtracking(idx+arr[idx])
            if idx - arr[idx] >= 0:
                backtracking(idx-arr[idx])
        backtracking(start)
        return self.rslt
    
   class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        dque, visited = collections.deque([start]), {start}
        while dque:
            curr =dque.popleft()
            if arr[curr] == 0: return True
            if curr + arr[curr] < len(arr) and curr+arr[curr] not in visited:
                visited.add(curr+arr[curr])
                dque.append(curr+arr[curr])
            if curr - arr[curr] >= 0 and curr - arr[curr] not in visited:
                visited.add(curr-arr[curr])
                dque.append(curr-arr[curr])
        return False
