class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        rslt, n = 0, len(arr)
        prefix = [0]*(n+1)
        for i in range(n): prefix[i+1] = prefix[i] ^ arr[i]
        for left in range(n-1):
            for right in range(left+1, n):
                if prefix[right+1]^prefix[left] == 0:
                    rslt += right-left
        return rslt





class Solution:
    def countTriplets(self, A):
        res = cur = 0
        count = {0: [1, 0]}
        for i, a in enumerate(A):
            cur ^= a
            n, total = count.get(cur, [0, 0])
            res += i * n - total
            count[cur] = [n + 1, total + i + 1]
        return res
