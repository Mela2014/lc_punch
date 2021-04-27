class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        cand = []
        rslt = 0
        for num in nums:
            idx = bisect.bisect_right(cand, 2*num)
            rslt = rslt + len(cand)-idx
            bisect.insort(cand, num)
        return rslt
