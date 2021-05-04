# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def helper(root):
            if not root: return 0, float("inf"), -float("inf")
            left = helper(root.left)
            right = helper(root.right)
            if left[2] < root.val < right[1]:
                return left[0]+right[0]+1,  min(left[1], root.val), max(root.val, right[2])
            else:
                return max(left[0], right[0]), -float("inf"), float("inf")
        temp = helper(root)
        return temp[0]
