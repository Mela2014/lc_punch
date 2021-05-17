class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[0] - x[1])
        rslt = quota = 0
        for actual, minimum in tasks:
            if minimum > quota:
                rslt += (minimum - quota)
                quota = minimum
            quota -= actual
        return rslt
