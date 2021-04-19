class CustomStack:

    def __init__(self, maxSize: int):
        self.cap = maxSize
        self.curSize = 0
        self.stack = [0]*maxSize

    def push(self, x: int) -> None:
        if self.curSize < self.cap:
            self.stack[self.curSize] = x
            self.curSize += 1

    def pop(self) -> int:
        if not self.curSize: return -1
        temp = self.stack[self.curSize-1]
        self.curSize -= 1
        return temp

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.curSize)):
            self.stack[i] += val
