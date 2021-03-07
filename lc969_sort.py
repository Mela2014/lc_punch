class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        s_arr, rslt, n = sorted(arr), [], len(arr)
        for i in range(n-1, 0, -1):
            idx = arr.index(s_arr[i])
            arr[:idx+1] = arr[:idx+1][::-1]
            arr[:i+1] = arr[:i+1][::-1]
            rslt.extend([idx+1, i+1])
        return rslt

    def pancakeSort(self, arr: List[int]) -> List[int]:
        n, rslt = len(arr), []
        for nmax in range(n, 1, -1):
            idx = arr.index(nmax)
            #arr = arr[nmax-1:idx:-1] + arr[:idx+1]
            arr = arr[:idx:-1] + arr[:idx]
            rslt.extend([idx+1, nmax])
        return rslt
