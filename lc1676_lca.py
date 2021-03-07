class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        def dfs(root):
            if not root: return None
            if root in nodes:
                return root
            left = dfs(root.left)
            right = dfs(root.right)
            if left and right:
                return root
            return left or right
        return dfs(root)
