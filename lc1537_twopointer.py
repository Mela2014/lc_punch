class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        idx1, idx2 = 0, 0
        max1, max2 = 0, 0
        while idx1 < l1 or idx2 < l2:
            if idx1 < l1 and (idx2 == l2 or nums1[idx1] < nums2[idx2]):
                max1 += nums1[idx1]
                idx1 += 1
            elif idx2 < l2 and (idx1 == l1 or nums1[idx1] > nums2[idx2]):
                max2 += nums2[idx2]
                idx2 += 1
            else:
                max1 = max(max1, max2) + nums1[idx1]
                max2 = max1
                idx1 += 1
                idx2 += 1
        return max(max1, max2)%(10**9+7)

        
