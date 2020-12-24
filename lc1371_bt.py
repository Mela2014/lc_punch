# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self.rslt = 0
        def helper(root):
            if not root: return 0, 0, True, 0
            if not root.right and not root.left: return root.val, root.val, True, root.val
            maxRR, minLR, isBSTR, ssumR = helper(root.right)
            maxRL, minLL, isBSTL, ssumL = helper(root.left)
            temp, ss = False, max(ssumR, ssumL)
            if not root.left and isBSTR and minLR > root.val:
                temp, ss, minLL = True, ssumR + root.val, root.val
            if not root.right and isBSTL and maxRL < root.val:
                temp, ss, maxRR = True, ssumL+root.val, root.val
            if isBSTR and isBSTL and maxRL < root.val < minLR:
                temp, ss= True, ssumR+ssumL+root.val
            self.rslt = max(self.rslt, ss)
            return maxRR, minLL, temp, ss
        _, _, _, rslt = helper(root)
        return self.rslt
