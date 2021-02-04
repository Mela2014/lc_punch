# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.rslt = 0
        def dfs(root):
            if not root: return -1
            left, right = dfs(root.left), dfs(root.right)
            # leaf's parent, put carmera
            if left == 0 or right == 0:
                self.rslt += 1
                return -2
            if left == -2 or right == -2:
                return -1
            else:
                return 0
        temp = dfs(root)
        return self.rslt + (temp == 0)
