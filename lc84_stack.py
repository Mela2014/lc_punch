class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, rslt = [], 0
        for i, h in enumerate(heights+[0]):
            start = i
            while stack and stack[-1][1] >= h:
                start, mh = stack.pop()
                rslt = max(rslt, (i - start)*mh)
            stack.append((start, h))
        return rslt
