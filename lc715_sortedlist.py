from sortedcontainers import SortedList
class RangeModule:
    def __init__(self):
        self.ranges = SortedList()
    def addRange(self, left: int, right: int) -> None:
        idl, idr = self.ranges.bisect_left(left), self.ranges.bisect_right(right)
        for _ in range(idr-idl):
            self.ranges.pop(idl)
        if idl%2 == 0: self.ranges.add(left)
        if idr%2 == 0: self.ranges.add(right)
    def queryRange(self, left: int, right: int) -> bool:
        idl, idr = self.ranges.bisect_right(left), self.ranges.bisect_left(right)
        return idl == idr and idl%2 == 1
    def removeRange(self, left: int, right: int) -> None:
        idl, idr = self.ranges.bisect_left(left), self.ranges.bisect_right(right)
        for _ in range(idr-idl):
            self.ranges.pop(idl)
        if idl%2 == 1: self.ranges.add(left)
        if idr%2 == 1: self.ranges.add(right)
