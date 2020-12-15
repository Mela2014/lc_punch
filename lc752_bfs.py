class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                t = int(node[i])
                for d in (-1, 1):
                    y = (t+d)%10
                    yield node[:i] + str(y) + node[i+1:]

        dd = set(deadends)
        queue, seen = collections.deque([('0000', 0 )]), {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in dd: continue
            for nei in neighbors(node):
                if nei not in seen and nei not in dd:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1
