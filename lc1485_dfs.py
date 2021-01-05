class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root: return None
        constructed = {}
        def dfs(root):
            if not root: return None
            if root in constructed: return constructed[root]
            copyroot = NodeCopy(root.val)
            constructed[root] = copyroot
            copyroot.left = dfs(root.left)
            copyroot.right = dfs(root.right)
            copyroot.random = dfs(root.random)
            return copyroot
        return dfs(root)
