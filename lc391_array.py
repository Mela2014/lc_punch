class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corners = set()
        for x1, y1, x2, y2 in rectangles:
            area += (y2-y1)*(x2-x1)
            for x, y in [(x1, y1), (x2, y2), (x1, y2), (x2, y1)]:
                if (x, y) in corners:
                    corners.remove((x, y))
                else:
                    corners.add((x, y))
        if len(corners) != 4:
            return False
        corners = sorted(corners)
        return area == (corners[-1][1]-corners[0][1])*(corners[-1][0] - corners[0][0])
