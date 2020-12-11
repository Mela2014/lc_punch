class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if not preorder or not inorder: return None
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        nodemap = {val:idx for idx, val in enumerate(inorder)}
        stk, head = [], None

        for val in preorder:
            if not head:
                head = TreeNode(val)
                stk.append(head)
            else:
                temp = TreeNode(val)
                if nodemap[val] < nodemap[stk[-1].val]:
                    stk[-1].left = temp
                else:
                    while stk and nodemap[stk[-1].val] < nodemap[val]:
                        last = stk.pop()
                    last.right = temp
                stk.append(temp)
        return head
