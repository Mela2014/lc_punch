class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        rslt = []
        # root
        rslt.append(root.val)
        if not root.left and not root.right:
            return rslt
        # left boundary
        if root.left:
            left = root.left
            while left.left or left.right:
                rslt.append(left.val)
                left = left.left if left.left else left.right
        # leaves
        stack = [root]
        while stack:
            temp = stack.pop()
            if not temp.left and not temp.right:
                rslt.append(temp.val)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        # right boundary
        temp = []
        if root.right:
            right = root.right
            while right.right or right.left:
                temp.append(right.val)
                right = right.right if right.right else right.left
        return rslt + temp[::-1]

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        def dfs_leftmost(node):
            if not node or not node.left and not node.right:
                return
            boundary.append(node.val)
            if node.left:
                dfs_leftmost(node.left)
            else:
                dfs_leftmost(node.right)

        def dfs_leaves(node):
            if not node:
                return
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
            dfs_leaves(node.left)
            dfs_leaves(node.right)

        def dfs_rightmost(node):
            if not node or not node.left and not node.right:
                return
            if node.right:
                dfs_rightmost(node.right)
            else:
                dfs_rightmost(node.left)
            boundary.append(node.val)

        if not root:
            return []
        boundary = [root.val]
        dfs_leftmost(root.left)
        dfs_leaves(root)
        dfs_rightmost(root.right)
        return boundary
