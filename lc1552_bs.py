class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        # def helper(mid):
        #     rslt, left = 1, 0
        #     for right in range(1, len(position)):
        #         if position[right]-position[left] >= mid:
        #             rslt += 1
        #             left = right
        #     return rslt
        # while left <= right:
        #     mid = (left + right)//2
        #     if helper(mid) >= m:
        #         left = mid + 1
        #     else:
        #         right = mid -  1

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:a
        def helper(mid):
            pre = position[0]
            for _ in range(m-1):
                pos = bisect.bisect_left(position, pre + mid)
                if pos == len(position):
                    return False
                pre = position[pos]
            return True
        left, right = 0, max(position)
        while left <= right:
            mid = (left + right)//2
            if helper(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
