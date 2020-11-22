class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        l_1, l_2 = len(nums1), len(nums2)
        dp = [nums1[0]*nums2[0]]
        for i in range(1, l_1): dp.append(max(dp[-1], nums1[i]*nums2[0]))
        for j in range(1, l_2):
            dp2 = [max(dp[0], nums1[0]*nums2[j])]
            for i in range(1, l_1):
                dp2.append(max(dp[i-1], dp2[i-1], dp[i], dp[i-1] + nums1[i]*nums2[j], nums1[i]*nums2[j]))
            dp = dp2
        return dp[-1]
