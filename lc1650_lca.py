class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parents = {}
        if not p or not q: return p or q
        while p:
            if p == q: return p
            parents[p] = p.parent
            p = p.parent
        while q:
            q = q.parent
            if q in parents:
                return q
        return None
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        tp, tq = p, q
        while tp != tq:
            if tp.parent:
                tp = tp.parent
            else:
                tp = q
            if tq.parent:
                tq = tq.parent
            else:
                tq = p
        return tp
