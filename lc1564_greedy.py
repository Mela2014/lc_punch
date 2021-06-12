class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()
        count = 0
        idx = 0
        for box in boxes[::-1]:
            if warehouse[idx] >= box:
                count += 1
                idx += 1
            if idx >= len(warehouse):
                return count
        return count
