class Block:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        self.kids = set()
class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sleft = Block()
        self.sright = Block(left = self.sleft)
        self.sleft.right = self.sright
        self.keyblock = {}
    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        preb = self.sleft
        if key in self.keyblock:
            preb = self.keyblock[key]
            preb.kids.remove(key)
        val = preb.val + 1
        if  preb.right.val == val:
            curb = preb.right
        else:
            curb = Block(val = val, left = preb, right = preb.right)
            preb.right.left, preb.right = curb, curb
        curb.kids.add(key)
        self.keyblock[key] = curb
        if not preb.kids and preb.val != 0:
            preb.left.right, preb.right.left = preb.right, preb.left
            preb.left, preb.right = None, None

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        preb = self.keyblock[key]
        preb.kids.remove(key)
        val = preb.val - 1
        if val == 0:
            curb = self.sleft
        elif preb.left.val == val:
            curb = preb.left
        else:
            curb = Block(val = val, left = preb.left, right = preb)
            preb.left.right, preb.left = curb, curb
        curb.kids.add(key)
        if curb.val:
            self.keyblock[key] = curb
        else:
            self.keyblock.pop(key)
        if not preb.kids and preb.val != 0:
            preb.left.right = preb.right
            preb.right.left = preb.left
            preb.left, preb.right = None, None
    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.sright.left.val == 0:
            return ""
        for kid in self.sright.left.kids:
            return kid
    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.sleft.right.val == 0:
            return ""
        for kid in self.sleft.right.kids:
            return kid
