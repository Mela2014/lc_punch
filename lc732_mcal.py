class MyCalendar:

    def __init__(self):
        self.booking = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.booking:
            if s < end and e > start:
                return False
        self.booking.append((start, end))
        return True
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None
class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        rslt, self.root = self.insert(self.root, start, end)
        return rslt

    def insert(self, root, start, end):
        if not root:
            return True, Node(start, end)
        if end <= root.start:
            rslt, root.left = self.insert(root.left, start, end)
            return rslt, root
        if start >= root.end:
            rslt, root.right = self.insert(root.right, start, end)
            return rslt, root
        return False, root
class MyCalendar:

    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        s, e = bisect.bisect_right(self.ends, start), bisect.bisect_left(self.starts, end)
        if s != e: return False
        bisect.insort(self.starts, start, s, e)
        bisect.insort(self.ends, end, s, e)
        return True

class MyCalendarTwo:

    def __init__(self):
        self.seen_once = []
        self.seen_twice = []

    def book(self, start: int, end: int) -> bool:
        for st, ed in self.seen_twice:
            if st < end and ed > start:
                return False
        for st, ed in self.seen_once:
            if st < end and ed > start:
                self.seen_twice.append((max(st, start), min(ed, end)))
        self.seen_once.append((start, end))
        return True
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None
        self.seen_twice = False
class MyCalendarTwo:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.check(self.root, start, end): return False
        self.root = self.insert(self.root, start, end)
        return True

    def check(self, root, start, end):
        if not root:
            return True
        if end <= root.start:
            return self.check(root.left, start, end)
        if start >= root.end:
            return self.check(root.right, start, end)
        if root.seen_twice: return False
        lefts, lefte, rights, righte = min(start, root.start), max(start, root.start), min(end, root.end), max(end, root.end)
        leftc = self.check(root.left, start, end)
        rightc = self.check(root.right, start, end)
        return leftc and rightc

    def insert(self, root, start, end):
        if start >= end:
            return root
        if not root:
            return Node(start, end)
        if end <= root.start:
            root.left = self.insert(root.left, start, end)
            return root
        if start >= root.end:
            root.right = self.insert(root.right, start, end)
            return root
        lefts, lefte, rights, righte = min(start, root.start), max(start, root.start), min(end, root.end), max(end, root.end)
        root.left = self.insert(root.left, lefts, lefte)
        root.right = self.insert(root.right, rights, righte)
        root.seen_twice = True
        root.start = lefte
        root.end = rights
        return root
class MyCalendarTwo:

    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        s, e = bisect.bisect_right(self.ends, start), bisect.bisect_left(self.starts, end)
        hp = []
        for i in range(s, e):
            while hp and hp[0] <= self.starts[i]:
                heapq.heappop(hp)
            heapq.heappush(hp, self.ends[i])
            if len(hp) > 1:
                return False
        bisect.insort(self.starts, start, s, e)
        bisect.insort(self.ends, end, s, e)
        return True



class MyCalendarThree:

    def __init__(self):
        self.booking = []
    def book(self, start: int, end: int) -> int:
        self.booking.append((start, 1))
        self.booking.append((end, -1))
        cnt, rslt = 0, 0
        self.booking.sort()
        for x, y in self.booking:
            cnt += y
            if cnt > rslt:
                rslt = cnt
        return rslt
class Node:
    def __init__(self, start, end, k):
        self.start = start
        self.end = end
        self.k = k
        self.right = self.left = None
class MyCalendarThree:

    def __init__(self):
        self.root = None
        self.k = 0
    def book(self, start: int, end: int) -> int:
        self.root = self.insert(self.root, start, end, 1)
        return self.k

    def insert(self, root, start, end, k):
        if start >= end:
            return root
        if not root:
            self.k = max(self.k, k)
            return Node(start, end, k)
        if end <= root.start:
            root.left = self.insert(root.left, start, end, k)
            return root
        if start >= root.end:
            root.right = self.insert(root.right, start, end, k)
            return root
        lefts, lefte, rights, righte = min(start, root.start), max(start, root.start), min(end, root.end), max(end, root.end)
        root.left = self.insert(root.left, lefts, lefte, root.k if lefts == root.start else k)
        root.right = self.insert(root.right, rights, righte, root.k if righte == root.end else k)
        root.k += k
        root.start = lefte
        root.end = rights
        self.k = max(self.k, root.k)
        return root
class MyCalendarThree:
    def __init__(self):
        self.starts = []
        self.ends = []
        self.booking = 0

    def book(self, start: int, end: int) -> int:
        s, e = bisect.bisect_right(self.ends, start), bisect.bisect_left(self.starts, end)
        bisect.insort(self.starts, start, s, e)
        bisect.insort(self.ends, end, s, e)
        # print(start, end, s, e, self.starts, self.ends)
        hp = [] # store end points
        for i in range(s, e + 1):
            while hp and hp[0] <= self.starts[i]:
                heapq.heappop(hp)
            heapq.heappush(hp, self.ends[i])
            if len(hp) > self.booking:
                self.booking = len(hp)
        return self.booking
