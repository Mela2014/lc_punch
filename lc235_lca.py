# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < q.val:
            q, p = p, q
        while root.val > p.val or root.val < q.val:
            if root.val > p.val:
                root = root.left
            else:
                root = root.right
        return root
