class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        prefix, rslt, temp = 0, 0, {0:1}
        for i, x in enumerate(A):
            prefix += x
            if prefix-S in temp:
                rslt += temp[prefix-S]
            temp[prefix] = temp.get(prefix, 0)+1
        return rslt
