class Solution:

    def __init__(self, w: List[int]):
        self.cumsum = []
        for i, n in enumerate(w):
            if i == 0: self.cumsum.append(n)
            else:
                self.cumsum.append(n + self.cumsum[-1])

    def pickIndex(self) -> int:
        t = random.randint(1, self.cumsum[-1])
        return self.binSearch(t)

    def binSearch(self, t):
        left, right = 0, len(self.cumsum)
        while left < right:
            mid = (left + right)//2
            if self.cumsum[mid] < t:
                left = mid+1
            else:
                right = mid
        return left



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
