class Node:
    def __init__(self, start, end):
        self.total = 0
        self.start, self.end = start, end
        self.left, self.right = None, None

class SegTree:
    def __init__(self, nums):
        self.nums = nums
        self.root = self.create_tree(0, len(self.nums)-1)

    def create_tree(self, start, end):
        if start == end:
            rslt = Node(start, end)
            rslt.total = self.nums[start]
            return rslt
        mid = (start + end)//2
        rslt = Node(start, end)
        rslt.left = self.create_tree(start, mid)
        rslt.right = self.create_tree(mid+1, end)
        rslt.total = rslt.left.total + rslt.right.total
        return rslt

    def update(self, i, val):
        def helper(root, i, val):
            if root.left == root.right:
                root.total = val
                return val
            mid = (root.start + root.end)//2
            if i <= mid:
                helper(root.left, i, val)
            else:
                helper(root.right, i, val)
            root.total = root.left.total + root.right.total
            return root.total
        helper(self.root, i, val)
    def sum_range(self, start, end):
        def helper(root, start, end):
            if root.start == start and root.end == end:
                return root.total
            mid = (root.start + root.end)//2
            if end <= mid:
                return helper(root.left, start, end)
            elif start > mid:
                return helper(root.right, start, end)
            else:
                return helper(root.left, start, mid) + helper(root.right, mid+1, end)
        return helper(self.root, start, end)

class NumArray:
    def __init__(self, nums: List[int]):
        self.segtree = SegTree(nums)

    def update(self, index: int, val: int) -> None:
        self.segtree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segtree.sum_range(left, right)
