# same as 538
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def helper(root, pre):
            if not root: return pre
            root.val += helper(root.right, pre)
            return helper(root.left, root.val)
        helper(root, 0)
        return root
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def helper(root, pre):
            if not root: return (0+pre, None)
            valr, right = helper(root.right, pre)
            vall, left = helper(root.left, valr+root.val)
            root.val += valr
            root.right =right
            root.left = left
            return (vall,root)
        _, root = helper(root, 0)
        return root
        
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
