class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        if X > len(customers):
            return sum(customers)
        i, curr, wind, cumsum= 0, 0, 0, 0
        for c, g in zip(customers, grumpy):
            cumsum += (1-g)*c
            if i < X:
                curr += g*c
            else:
                curr += g*c - grumpy[i-X]*customers[i-X]
            wind = max(wind, curr)
            i += 1
        return cumsum + wind
