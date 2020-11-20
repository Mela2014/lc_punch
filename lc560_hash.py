class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        keeper = {0:1}
        rslt, temp = 0, 0
        for num in nums:
            temp += num
            rslt += keeper.get(temp-k, 0)
            keeper[temp] = keeper.get(temp, 0) +1
        return rslt