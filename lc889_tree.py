class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre or not post: return None
        root = TreeNode(pre[0])
        if len(pre) > 1:
            idx = post.index(pre[1])
            root.left = self.constructFromPrePost(pre[1:idx+2], post[:idx+1])
            root.right = self.constructFromPrePost(pre[idx+2:], post[idx+1:-1])
        return root
        
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        nodemap = {val:i for i, val in enumerate(post)}
        stk, root = [], None
        for val in pre:
            if not root:
                root = TreeNode(val)
                stk.append(root)
            else:
                temp = TreeNode(val)
                if nodemap[val] < nodemap[stk[-1].val]:
                    stk[-1].left = temp
                else:
                    while stk and nodemap[val] > nodemap[stk[-1].val]:
                        last = stk.pop()
                    stk[-1].right = temp
                stk.append(temp)
        return root
