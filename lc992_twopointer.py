class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        memo1, memo2, left, right, rslt = collections.defaultdict(int), collections.defaultdict(int), 0, 0, 0
        for it in A:
            memo1[it] += 1
            memo2[it] += 1
            while len(memo1) > K:
                memo1[A[left]] -= 1
                if memo1[A[left]] == 0: del memo1[A[left]]
                left += 1
            while len(memo2) >= K:
                memo2[A[right]] -= 1
                if memo2[A[right]] == 0: del memo2[A[right]]
                right += 1
            rslt += right-left
        return rslt

class Solution:
    def atMostK(self, A, K):
        memo, left, rslt = collections.defaultdict(int), 0, 0
        for right, it in enumerate(A):
            memo[it] += 1
            while len(memo) > K:
                memo[A[left]] -= 1
                if memo[A[left]] == 0: del memo[A[left]]
                left += 1
            rslt += right-left + 1
        return rslt
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        if not A: return 0
        return self.atMostK(A, K) - self.atMostK(A, K - 1)


