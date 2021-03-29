class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        c1, c2 = collections.Counter(nums1), collections.Counter(nums2)
        def helper(c1, c2):
            rslt, temp = 0, 0
            for k, v in c1.items():
                rslt += v*c2[k]*(c2[k]-1)//2

                for c in c2:
                    if c < k and (k*k)%c == 0:
                        rslt += v*c2[c]*c2[(k*k)//c]
            return rslt
        return helper(c1, c2) + helper(c2, c1)
