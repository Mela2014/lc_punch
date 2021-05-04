class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        maps = {}
        def get_parents(curr, prev):
            if curr:
                maps[curr] = prev
                get_parents(curr.left, curr)
                get_parents(curr.right, curr)
        get_parents(root, None)
        queue = collections.deque([(target, 0)])
        visited = {target}
        while queue:
            if queue[0][1] == K:
                return [x.val for x, y in queue]
            node, dist = queue.popleft()
            for nxt in [node.left, node.right, maps[node]]:
                if nxt and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, dist + 1))
        return []
        
