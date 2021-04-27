class Segtree:
    def __init__(self, n):
        self.n = n
        self.seg_tree = [0]*(2*n)

    def update(self, idx):
        idx = self.n+idx
        self.seg_tree[idx] += 1
        while idx > 1:
            self.seg_tree[idx>>1] = self.seg_tree[idx] + self.seg_tree[idx^1]
            idx >>= 1

    def sumRange(self, idx):
        l = self.n
        r = self.n + idx
        rslt = -self.seg_tree[r]
        while l <= r:
            if l&1:
                rslt += self.seg_tree[l]
                l += 1
            if r&1 == 0:
                rslt += self.seg_tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        return rslt

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        maps = {val:i for i, val in enumerate(sorted(nums))}
        n = len(nums)
        segtree = Segtree(n)
        rslt = [0]*n
        for i in range(n-1, -1, -1):
            segtree.update(maps[nums[i]])
            rslt[i] = segtree.sumRange(maps[nums[i]])
        return rslt
