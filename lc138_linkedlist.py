"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        curr = head
        while curr:
            copy = Node(curr.val, curr.next)
            curr.next = copy
            curr = copy.next
        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        curr, rslt = head, head.next
        while curr:
            temp = curr.next
            curr.next = temp.next
            temp.next = temp.next.next if temp.next else None
            curr = curr.next
        return rslt

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
