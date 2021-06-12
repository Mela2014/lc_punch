class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        # find k
        left, right = 0, max(inventory)
        helper = lambda k: sum(max(0, i-k) for i in inventory)
        while left <= right:
            mid = (left+right)//2
            if helper(mid) < orders:
                right = mid -1
            else:
                left = mid + 1
        rslt = sum((i+right+1)*(i-right)//2 for i in inventory if i > right)
        return (rslt - (helper(right)-orders)*(right+1))%(10**9+7)
        
