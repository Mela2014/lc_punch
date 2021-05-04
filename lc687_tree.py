# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.rslt = 0
        def helper(root):
            if not root: return 0
            left = helper(root.left)
            right = helper(root.right)
            left_l, right_l = 0, 0
            if root.left and root.left.val == root.val:
                left_l = left + 1
            if root.right and root.right.val == root.val:
                right_l = right + 1
            self.rslt = max(self.rslt, left_l+right_l)
            return max(left_l, right_l)
        helper(root)
        return self.rslt
