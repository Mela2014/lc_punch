class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort()
        target, rm = divmod(sum(nums), k)
        if rm or target < nums[-1]: return False
        def dfs():
            if not nums: return True
            right = nums.pop()
            for i, ttt in enumerate(tt_list):
                if ttt + right <= target:
                    tt_list[i] += right
                    if dfs(): return True
                    tt_list[i] -= right
                if ttt == 0: break
            nums.append(right)
            return False
        tt_list = [0]*k
        return dfs()
