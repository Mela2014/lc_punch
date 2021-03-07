# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        seen, parents = set(), {root:None}
        while p not in parents or q not in parents:
            parent = stack.pop()
            if parent.left:
                parents[parent.left] = parent
                stack.append(parent.left)
            if parent.right:
                parents[parent.right] = parent
                stack.append(parent.right)
        cands = set()
        while p:
            cands.add(p)
            p = parents[p]
        while q not in cands:
            q = parents[q]
        return q
