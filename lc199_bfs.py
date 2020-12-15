class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = collections.deque([root])
        rslt = []
        while queue:
            lth = len(queue)
            for _ in range(lth):
                temp = queue.popleft()
                if temp.left: queue.append(temp.left)
                if temp.right: queue.append(temp.right)
            rslt.append(temp.val)
        return rslt
