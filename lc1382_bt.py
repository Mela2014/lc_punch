# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        rslt = []
        def preorder(l, r):
            if r == l:
                return None
            mid = (l+r)//2
            root = TreeNode(rslt[mid])
            root.left = preorder(l, mid)
            root.right = preorder(mid+1, r)
            return root
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            rslt.append(root.val)
            inorder(root.right)
        inorder(root)
        return preorder(0, len(rslt))
