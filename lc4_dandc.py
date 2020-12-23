class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return None
        l1, l2 = len(nums1), len(nums2)
        if (l1+l2)%2 ==1:
            return self.findKth(nums1, nums2, 0, 0, (l1+l2)//2 + 1)
        else:
            left = self.findKth(nums1, nums2, 0, 0, (l1+l2)//2)
            right = self.findKth(nums1, nums2, 0, 0, (l1+l2)//2+1)
            return (left+right)/2

    def findKth(self, nums1, nums2, loc1, loc2, k):
        if loc1 == len(nums1):
            return nums2[loc2 + k -1]
        if loc2 == len(nums2):
            return nums1[loc1 + k -1]
        if k == 1:
            return min(nums1[loc1], nums2[loc2])

        p1 = nums1[loc1 + k//2 - 1] if loc1 + k//2 - 1 < len(nums1) else None
        p2 = nums2[loc2 + k//2 - 1] if loc2 + k//2 - 1 < len(nums2) else None

        if p2 is None or (p1 is not None and p1 < p2):
            return self.findKth(nums1, nums2, loc1+k//2, loc2, k - k//2)
        return self.findKth(nums1, nums2, loc1, loc2 + k//2, k - k//2)
