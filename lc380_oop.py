class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hold = {}
        self.idx = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hold:
            return False
        self.hold[val] = len(self.idx)
        self.idx.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.hold :
            self.idx[self.hold[val]] = self.idx[-1]
            self.hold[self.idx[-1]] = self.hold[val]
            self.idx.pop()
            del self.hold[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.idx)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
