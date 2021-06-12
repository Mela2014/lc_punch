class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        left, right = float("inf"), 0
        rslt = float("inf")
        for num in nums:
            if num%2:
                num = num*2
            heapq.heappush(heap, -num)
            left = min(left, num)
        while True:
            right = -heapq.heappop(heap)
            if right-left < rslt:
                rslt = right-left
            if right%2 == 0:
                heapq.heappush(heap, -right//2)
                left = min(left, right//2)
            else:
                break
        return rslt
