class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # Dijkstra: node is labeled by the row index sequences
        nrow, ncol = len(mat), len(mat[0])
        visited = {(0,)*nrow}
        heap = [(sum(row[0] for row in mat), (0,)*nrow)]
        for i in range(k):
            cur_val, cur_node = heapq.heappop(heap)
            for j in range(nrow):
                if cur_node[j] + 1 < ncol:
                    nxt_val = cur_val - mat[j][cur_node[j]] + mat[j][cur_node[j]+1]
                    nxt_node = cur_node[:j]+(cur_node[j]+1, )+ cur_node[j+1:]
                    if nxt_node not in visited:
                        visited.add(nxt_node)
                        heapq.heappush(heap, (nxt_val, nxt_node))
        return cur_val
