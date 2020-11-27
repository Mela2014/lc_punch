class StockSpanner:

    def __init__(self):
        self.last = [(float('inf'), -1)]
        self.curr = 0


    def next(self, price: int) -> int:
        while self.last and price >= self.last[-1][0]:
            self.last.pop()
        temp = self.curr if not self.last else self.last[-1][1]+1
        self.last.append((price, self.curr))
        self.curr += 1
        return self.curr - temp
