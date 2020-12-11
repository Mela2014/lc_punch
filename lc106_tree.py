class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        nodemap = {val:idx for idx, val in enumerate(inorder)}
        stk, head = [], None
        for node in postorder[::-1]:
            if not head:
                head = TreeNode(node)
                stk.append(head)
            else:
                temp = TreeNode(node)
                if nodemap[node] > nodemap[stk[-1].val]:
                    stk[-1].right = temp
                else:
                    while stk and nodemap[stk[-1].val] > nodemap[node]:
                        last = stk.pop()
                    last.left = temp
                stk.append(temp)
        return head

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder: return None
        root = TreeNode(postorder[-1])
        idx = inorder.index(root.val)
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        return root
