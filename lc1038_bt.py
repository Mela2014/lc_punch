# same as 538
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

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        curr, stk, last = root, [], 0
        while stk or curr:
            while curr:
                stk.append(curr)
                curr = curr.right
            temp = stk.pop()
            temp.val += last
            last = temp.val
            curr = temp.left
        return root
