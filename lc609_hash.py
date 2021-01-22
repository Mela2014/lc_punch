class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        nodemap = {}
        def dfs(curr):
            if not curr: return None
            if curr in nodemap: return nodemap[curr]
            copy = Node(curr.val)
            nodemap[curr] = copy
            copy.next = dfs(curr.next)
            copy.random  = dfs(curr.random)
            return copy
        return dfs(head)

# Follow up:
# - DFS: as we must arrive at the file, like a leaf node in the tree, and we don't care the directory unless there's files in there, DFS will be a better choice, as DFS can resuse the shared path before leaving that directory.
# - 1. Use File size. 2. Compare random sampled rows. 3. Check MD5 or SHA256 hash, 4 check byte by byte
