class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        idxa, idxb, na, nb = 0, 0, len(firstList), len(secondList)
        rslt = []
        while idxa < na and idxb < nb:
            leftb = max(firstList[idxa][0], secondList[idxb][0])
            rightb = min(firstList[idxa][1], secondList[idxb][1])
            if leftb <= rightb:
                rslt.append([leftb, rightb])
            if firstList[idxa][1] < secondList[idxb][1]:
                idxa += 1
            else:
                idxb += 1
        return rslt
