class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        currD, num = 0, ""
        root = None
        stk = []
        for c in S+'-':
            if c == "-":
                if not num:
                    currD += 1
                else:
                    curr = TreeNode(int(num))
                    if not root:
                        root = curr
                    elif stk[-1][1] < currD:
                        stk[-1][0].left = curr
                    else:
                        while stk[-1][1] >= currD:
                            stk.pop()
                        stk[-1][0].right = curr
                    stk.append((curr, currD))
                    num = ""
                    currD = 1
            else:
                num += c
        return root
