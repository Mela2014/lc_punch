class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue, left, rslt = collections.deque([root]), 1, []
        while queue:
            lq = len(queue)
            temp = [0]*lq
            for i in range(lq):
                curr = queue.popleft()
                if left == 1: temp[i] = curr.val
                else:temp[lq-i-1] = curr.val
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            left = (left+1)%2
            rslt.append(temp)
        return rslt
