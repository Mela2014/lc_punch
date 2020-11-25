class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        mmap = collections.defaultdict(list)
        for i, m in enumerate(manager):
            if m != -1:
                mmap[m].append(i)
        def dfs(mid):
            rslt = 0
            for sub in mmap[mid]:
                rslt = max(rslt, informTime[mid] + dfs(sub))
            return rslt
        return dfs(headID)
