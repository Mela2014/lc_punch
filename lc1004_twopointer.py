class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left, cnt, rslt = 0, 0, 0
        for right, c in enumerate(A):
            if c == 0:
                cnt += 1
            while cnt > K:
                cnt -= 1-A[left]
                left += 1
            rslt = max(rslt, right-left + 1)
        return rslt
