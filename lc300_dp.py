class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            temp = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    temp = max(temp, dfs(j)+1)
            return temp
        rslt = 0
        for i in range(len(nums)):
            rslt = max(rslt, dfs(i))
        return rslt

    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            idx = bisect.bisect_left(sub, num)
            if idx < len(sub):
                sub[idx] = num
            else:
                sub.append(num)
        return len(sub)
        
    def lengthOfLIS(self, nums:List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if dp[j] < dp[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)



    def lengthOfLIS(self, nums: List[int]) -> int:
        def bisearch(arr, target):
            left, right = 0, len(arr)-1
            while left <= right:
                mid = (left + right)//2
                if arr[mid] < target:
                    left = mid
                else:
                    right = mid - 1
                if (left+right)//2 == mid:
                    left += 1
            return left
        sub = []
        for num in nums:
            idx = bisearch(sub, num)
            if idx < len(sub):
                sub[idx] = num
            else:
                sub.append(num)
        return len(sub)
