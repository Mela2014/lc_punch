class Solution:
# dfs+memo /dp
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @lru_cache(None)
        def dfs(i,j):
            if j<=i:
                return 0
            res = float('inf')
            for k in range(i,j):
                res = min(dfs(i,k)+dfs(k+1,j)+max(arr[i:k+1])*max(arr[k+1:j+1]),res)
            return res
        return dfs(0,len(arr)-1)

#https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/951938/Don't-overthink-about-trees.-It's-a-DPGreedy-problem.
# greedy
    def mctFromLeafValues(self, A):
        res = 0
        while len(A) > 1:
            i = A.index(min(A))
            res += min(A[i - 1:i] + A[i + 1:i + 2]) * A.pop(i)
        return res

#https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/478708/RZ-Summary-of-all-the-solutions-I-have-learned-from-Discuss-in-Python
    def mctFromLeafValues(self, A):
        res = 0
        stack = [float("inf")]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res
