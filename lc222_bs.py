class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        left, depth = root, 0
        while left.left:
            left = left.left
            depth += 1
        left, right = (1<<depth), (1<<(depth+1))-1
        while left <= right:
            mid = (left + right)//2
            if self.check(mid, root):
                left = mid+1
            else:
                right = mid -1
        return right

    def check(self, mid, root):
        path = bin(mid)[3:]
        for x in path:
            if x == "0":
                root = root.left
            else:
                root = root.right
            if not root:
                return False
        return True
            
