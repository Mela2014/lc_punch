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
