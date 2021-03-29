class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        lines = []
        for l, r, h in buildings:
            lines.append([l, h])
            lines.append([r, -h])
        lines.sort(key = lambda x: (x[0], -x[1]))
        heap = [0]
        rslt = []
        for x, h in lines:
            if h > 0:
                # start
                if h > -heap[0]:
                    rslt.append([x, h])
                heapq.heappush(heap, -h)
            else:
                # end
                heap.remove(h)
                heapq.heapify(heap)
                if -h > -heap[0]:
                    rslt.append([x, -heap[0]])
        return rslt
