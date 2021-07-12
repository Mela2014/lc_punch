class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.holder = [[] for _ in range(512)]

    def add(self, key: int) -> None:
        if self.contains(key):
            return True
        self.holder[key%512].append(key)
        return False


    def remove(self, key: int) -> None:
        hh = key%512
        i = 0
        while i < len(self.holder[hh]):
            if self.holder[hh][i] == key:
                self.holder[hh][i], self.holder[hh][-1] = self.holder[hh][-1], self.holder[hh][i]
                self.holder[hh].pop()
                break
            i += 1
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hh = key%512
        i = 0
        while i < len(self.holder[hh]):
            if self.holder[hh][i] == key:
                return True
            i += 1
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
