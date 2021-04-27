from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        maps = SortedList([0])
        rslt, cumsum = 0, 0
        for num in nums:
            cumsum += num
            left = maps.bisect_left(cumsum-upper)
            right = maps.bisect_right(cumsum-lower)
            if right > left:
                rslt += right-left
            maps.add(cumsum)
        return rslt
