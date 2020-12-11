class Solution:
    def findleftlarge(self, root):
        while root.right:
            root = root.right
        return root.val
    def findrightsmall(self, root):
        while root.left:
            root = root.left
        return root.val
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            if root.right:
                root.val = self.findrightsmall(root.right)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.findleftlarge(root.left)
                root.left = self.deleteNode(root.left, root.val)
        return root
