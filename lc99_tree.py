# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def recoverTree(self, root: TreeNode) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     order = self.inorder(root)
    #     y, x = None, None
    #     for i in range(len(order)-1):
    #         if order[i+1] < order[i]:
    #             y = order[i+1]
    #             if x is None:
    #                 x = order[i]
    #             else:
    #                 break
    #     stack = [root]
    #     while stack:
    #         temp = stack.pop()
    #         if temp.val in (x, y):
    #             temp.val = x if temp.val == y else y
    #         if temp.left: stack.append(temp.left)
    #         if temp.right:stack.append(temp.right)
    # def inorder(self, root):
    #     if not root: return []
    #     return self.inorder(root.left) +[root.val] + self.inorder(root.right)

    def recoverTree(self, root: TreeNode) -> None:
        self.x, self.y, self.pre = None, None, None
        def inorder(root):
            if not root: return
            inorder(root.left)
            if self.pre and root.val < self.pre.val:
                self.y = root
                if not self.x:
                    self.x = self.pre
            self.pre = root
            inorder(root.right)
        inorder(root)
        self.x.val, self.y.val = self.y.val, self.x.val

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr, stack = root, []
        x = y = pre = None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if pre and curr.val < pre.val:
                y = curr
                if x is None:
                    x = pre
                else: break
            pre = curr
            curr = curr.right
        x.val, y.val = y.val, x.val
