class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        left, lnote, rslt = -1, "L", ""
        for right, do in enumerate(dominoes+"R"):
            if do == ".":
                continue
            mid = right-left-1
            if left >= 0:
                rslt += lnote
            if do == lnote:
                rslt += mid*lnote
            elif lnote == "L" and do == "R":
                rslt += mid*"."
            else:
                rslt += "R"*(mid//2)+"."*(mid%2)+"L"*(mid//2)
            left = right
            lnote = do
        return rslt
