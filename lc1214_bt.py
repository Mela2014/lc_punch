# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        stk, pool = [], set()
        while stk or root1:
            while root1:
                stk.append(root1)
                root1 = root1.left
            temp = stk.pop()
            pool.add(temp.val)
            root1 = temp.right
        stk = [root2]
        while stk:
            temp = stk.pop()
            if target-temp.val in pool:
                return True
            if temp.right: stk.append(temp.right)
            if temp.left: stk.append(temp.left)
        return False
