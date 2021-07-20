class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        d = len(nums)//k
        count = collections.Counter(nums)
        if max(count.values()) > k: return -1

        @lru_cache(None)
        def dfs(curr):
            if not curr:
                return 0
            rslt = float("inf")

            for comb in itertools.combinations(set(curr), d):
                remain = list(curr)
                for t in comb:
                    remain.remove(t)
                rslt = min(rslt, max(comb)-min(comb) + dfs(tuple(remain)))
            return rslt
        return dfs(tuple(nums))
