class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        diff = sum(nums1) - sum(nums2)
        if diff < 0:
            nums1, nums2 = nums2, nums1
            diff = -diff
        quota = collections.Counter([x-1 for x in nums1]+[6-x for x in nums2])
        count, change = 0, 5
        while diff > 0:
            if change == 0: return -1
            if (diff-1)//change+1 <= quota[change]:
                return count + (diff-1)//change + 1
            else:
                diff, count = diff-change*quota[change], count + quota[change]
                change -= 1
        return count

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        diff = sum(nums1) - sum(nums2)
        if not diff: return 0
        if diff < 0:
            nums1, nums2 = nums2, nums1
            diff = -diff
        nums1.sort(reverse = True)
        nums2.sort()
        count, idx1, idx2, l1, l2 = 0, 0, 0, len(nums1), len(nums2)
        while idx1 < l1 or idx2 < l2:
            if diff <= 0:
                return count
            if idx1 < l1 and diff <= nums1[idx1]-1:
                return count + 1
            if idx2 < l2 and diff <= 6 - nums2[idx2]:
                return count + 1
            sub1 = (nums1[idx1]-1) if idx1 < l1 else 0
            sub2 = (6 - nums2[idx2]) if idx2 < l2 else 0
            if sub1 >= sub2 and idx1 < l1:
                diff -= sub1
                idx1 += 1
            else:
                diff -= sub2
                idx2 += 1
            count += 1
        return count if diff <= 0 else -1
