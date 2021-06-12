from sortedcontainers import SortedList
class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.win = collections.deque([0]*m)
        self.o_win = SortedList([0]*m)
        self.sum_k, self.sum_m_k = 0, 0

    def addElement(self, num: int) -> None:
        self.win.append(num)
        # update out of window ele
        oow = self.win.popleft()
        i_oow = self.o_win.bisect_right(oow)
        if i_oow <= self.k:
            self.sum_k = self.sum_k - oow + self.o_win[self.k]
        if i_oow <= self.m - self.k:
            self.sum_m_k = self.sum_m_k - oow + self.o_win[self.m-self.k]
        self.o_win.remove(oow)
        # update new ele
        i_new = self.o_win.bisect_right(num)
        if i_new < self.k:
            self.sum_k = self.sum_k - self.o_win[self.k-1] + num
        if i_new < self.m-self.k:
            self.sum_m_k = self.sum_m_k - self.o_win[self.m-self.k-1] + num
        self.o_win.add(num)
        return

    def calculateMKAverage(self) -> int:
        # print(self.o_win, self.sum_m_k, self.sum_k)
        if self.o_win[0] == 0:
            return -1
        return (self.sum_m_k - self.sum_k) // (self.m - self.k*2)
