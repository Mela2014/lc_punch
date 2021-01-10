class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.mark = 0
        def dfs(root, p, q):
            if not root: return None
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            if root == p or root == q:
                self.mark += 1
                return root
            if left and right:
                return root
            else:
                return left or right
        rslt = dfs(root, p, q)
        return rslt if self.mark == 2 else None
