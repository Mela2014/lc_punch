class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, 1, x1, x2))
            events.append((y2, -1, x1, x2))
        events.sort()

        def cal_x_len():
            l_x, lastx = 0, 0
            for x1, x2 in active:
                lastx = max(lastx, x1)
                l_x += max(0, x2 -lastx)
                lastx = max(lastx, x2)
            return l_x
        active = []
        lasty = events[0][0]
        rslt = 0
        for y, status, x1, x2 in events:
            rslt += cal_x_len()*(y-lasty)
            if status == 1:
                bisect.insort(active, (x1, x2))
            else:
                active.remove((x1, x2))
            lasty = y
        return rslt % (10**9 + 7)
