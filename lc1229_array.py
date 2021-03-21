class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        n1, n2 = len(slots1), len(slots2)
        i, j = 0, 0
        while i < n1 and j < n2:
            left, right = max(slots1[i][0], slots2[j][0]), min(slots1[i][1], slots2[j][1])
            if right - left >= duration:
                    return [left, left +duration]
            elif slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []
