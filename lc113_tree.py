class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        rslt = []
        def backtracking(root, val, path):
            if not root.left and not root.right and val == targetSum and path:
                rslt.append(path)
            else:
                if root.left:
                    backtracking(root.left, val+root.left.val, path+[root.left.val])
                if root.right:
                    backtracking(root.right, val+root.right.val, path+[root.right.val])
        if not root: return rslt
        backtracking(root, root.val, [root.val])
        return rslt 
