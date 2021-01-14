class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cands, curr, rslt= set(nums), 1, 0
        for cand in cands:
            curr = 1
            if cand-1 not in cands:
                while cand+1 in cands:
                    cand = cand+1
                    curr += 1
                rslt = max(rslt, curr)
        return rslt
