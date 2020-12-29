class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        presum = [0]
        for num in A: presum.append(presum[-1]+num)
        rslt, dque = len(A)+1, collections.deque()
        for idx, pre in enumerate(presum):
            while dque and pre <= presum[dque[-1]]:
                dque.pop()
            dque.append(idx)
            while pre - presum[dque[0]] >= K:
                rslt = min(rslt, idx-dque.popleft())
        return -1 if rslt == len(A)+1 else rslt
