class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr): return m
        border, rslt =[0]*(len(arr)+2), -1
        for i, idx in enumerate(arr):
            left = right = idx
            if border[right + 1] > 0: right = border[right + 1]
            if border[left - 1] > 0: left = border[left - 1]
            border[left], border[right] = right, left
            if (right-idx==m) or (idx-left ==m): rslt = i
        return rslt

# deque + hashtable

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == m: return m
        dp = [0]*(len(arr)+1)
        for i, idx in enumerate(arr): dp[idx] = i+1
        dque, rslt = collections.deque(), -1
        for i in range(1, len(dp)):
            while dque and dp[dque[-1]] < dp[i]:
                dque.pop()
            while dque and i- dque[0] >= m:
                dque.popleft()
            dque.append(i)
            if i < m: continue
            left, right, maxDay = float("inf"), float("inf"), dp[dque[0]]
            if i-m >= 1: left = dp[i-m]
            if i+1 <= len(arr): right = dp[i+1]
            if maxDay < left and maxDay < right:
                rslt = max(rslt, min(left,right)-1)
        return rslt



# too slow, binary search
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr): return m
        cands = [0, len(arr)+1]
        for i, idx in enumerate(arr[::-1]):
            temp = bisect.bisect(cands, idx)
            cands.insert(temp, idx)
            if cands[temp]-cands[temp-1]-1 == m or cands[temp+1]- cands[temp]-1 == m:
                return len(arr)-i-1
        return -1
