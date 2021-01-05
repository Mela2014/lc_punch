class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums[(0+len(nums))//2]
        left = [l for l in nums if l > pivot]
        mid = [m for m in nums if m == pivot]
        right = [r for r in nums if r < pivot]
        if len(left) >= k:
            return self.findKthLargest(left, k)
        elif len(left)+len(mid) >= k:
            return pivot
        else:
            return self.findKthLargest(right, k-len(left)-len(mid))


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            pivot, l = (left+right)//2, left
            nums[pivot], nums[right] = nums[right], nums[pivot]
            for i in range(left, right):
                if nums[i] >= nums[right]:
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1
            nums[right], nums[l] = nums[l], nums[right]
            return l
        def select(left, right, k):
            if left == right:
                return nums[k]
            pivot = partition(left, right)
            if k == pivot:
                return nums[k]
            elif k < pivot:
                return select(left, pivot-1, k)
            else:
                return select(pivot+1, right, k)
        return select(0, len(nums)-1, k-1)
