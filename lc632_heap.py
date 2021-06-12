class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        right = max(row[0] for row in nums)
        rslt = (0, float("inf"))
        heapq.heapify(heap)
        while True:
            left, ir, ic = heapq.heappop(heap)
            if right-left < rslt[1]-rslt[0]:
                rslt = (left, right)
            if ic + 1 == len(nums[ir]):
                return rslt
            nxt = nums[ir][ic+1]
            right = max(right, nxt)
            heapq.heappush(heap, (nxt, ir, ic+1))
