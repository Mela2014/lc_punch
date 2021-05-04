class Solution:
    def pathSum(self, nums: List[int]) -> int:
        maps = {num//10: num%10 for num in nums}
        self.rslt = 0
        def dfs(idx, curr):
            if idx not in maps: return
            curr += maps[idx]
            depth, loc = divmod(idx, 10)
            left = (depth+1)*10+loc*2-1
            right = left + 1
            if left not in maps and right not in maps:
                self.rslt += curr
            else:
                dfs(left, curr)
                dfs(right, curr)
        dfs(nums[0]//10, 0)
        return self.rslt
