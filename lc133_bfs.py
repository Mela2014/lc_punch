class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        newnode = Node(node.val)
        if not node.neighbors: return newnode
        queue = deque([node])
        amap = {node.val: newnode}
        visited = set()
        while queue:
            onode = queue.popleft()
            nnode = amap[onode.val]
            nnode.neighbors = []
            for n in onode.neighbors:
                if n.val not in amap:
                    amap[n.val] = Node(n.val)
                nnode.neighbors.append(amap[n.val])
                if n.val not in visited:
                    queue.append(n)
            visited.add(nnode.val)
        return newnode
