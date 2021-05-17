class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = min(nums), max(nums)
        if n < 2 or left == right: return 0
        s_bkts = (right - left) //(n-1) or 1
        n_bkts = (right-left)//s_bkts + 1
        bkts = [[float("inf"), -float("inf")] for _ in range(n_bkts)]
        for num in nums:
            idx = (num-left)//s_bkts
            bkts[idx] = min(num, bkts[idx][0]), max(num, bkts[idx][1])
        last, rslt = None, 0
        for i in range(n_bkts):
            if not last:
                last = bkts[i][1]
            elif bkts[i][0] < float("inf"):
                rslt = max(rslt, bkts[i][0]-last)
                last = bkts[i][1]
        return rslt
