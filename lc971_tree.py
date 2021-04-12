# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        stack, i, rslt = [root], 0, []
        while stack:
            curr = stack.pop()
            if not curr: continue
            if curr.val != voyage[i]: return [-1]
            i += 1
            if curr.left and curr.left.val != voyage[i]:
                curr.left, curr.right = curr.right, curr.left
                rslt.append(curr.val)
            stack.append(curr.right)
            stack.append(curr.left)
        return rslt
