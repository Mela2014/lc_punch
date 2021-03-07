# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:

        def lca(root, p, q):
            if not root: return None
            if root.val == p or root.val == q:
                return root
            left = lca(root.left, p, q)
            right = lca(root.right, p, q)
            if left and right:
                return root
            return left or right
        pqlca = lca(root, p, q)
        queue = collections.deque([pqlca])
        lq, lp, level = 0, 0, 0
        while queue:
            l = len(queue)
            for _ in range(l):
                temp = queue.popleft()
                if temp.val == q:
                    lq = level
                if temp.val == p:
                    lp = level
                if temp.left: queue.append(temp.left)
                if temp.right: queue.append(temp.right)
            level += 1
        return lq+lp
