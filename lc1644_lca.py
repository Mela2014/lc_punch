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
            return left or right

        rslt = dfs(root, p, q)
        return rslt if self.mark == 2 else None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root:None}
        stack = [root]
        while stack:
            parent = stack.pop()
            if parent.right:
                parents[parent.right] = parent
                stack.append(parent.right)
            if parent.left:
                parents[parent.left] = parent
                stack.append(parent.left)
        cands = set()
        if p not in parents or q not in parents:
            return None
        while p in parents:
            cands.add(p)
            p = parents[p]
        while q in parents:
            if q in cands:
                return q
            q = parents[q]
