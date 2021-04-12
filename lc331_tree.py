class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stk = []
        temp = preorder.split(",")
        i = 0
        while i < len(temp):
            if temp[i] == "#":
                if not stk or stk[-1] != "#":
                    stk.append("#")
                    i += 1
                elif len(stk) < 2:
                    return False
                else:
                    stk.pop()
                    stk.pop()
            else:
                stk.append(temp[i])
                i += 1
        return stk == ["#"]

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slot = 1
        for i, c in enumerate(preorder+","):
            if c == ",":
                slot -= 1
                if slot < 0: return False
                if preorder[i-1] != "#": slot += 2
        return slot == 0
