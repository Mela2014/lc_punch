class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        x, y = 0, 0
        r1, r2 = 0, 0
        while x < l1 or y < l2:
            if x < l1 and (y == l2 or nums1[x] < nums2[y]):
                r1 += nums1[x]
                x += 1
            elif y < l2 and (x == l1 or nums1[x] > nums2[y]):
                r2 += nums2[y]
                y += 1
            else:
                r1 = max(r1, r2) + nums1[x]
                r2 = r1
                x += 1
                y += 1
        return max(r1, r2)%(10**9+7)

        
