# hash function + collision handling(chaining)
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [[] for _ in range(200)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hs = key % 200
        if len(self.table[hs]) == 0:
            self.table[hs].append((key, value))
            return
        for i, v in enumerate(self.table[hs]):
            if v[0] == key:
                self.table[hs][i] = (key, value)
                return
        self.table[hs].append((key, value))


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hs = key % 200
        if len(self.table[hs]) == 0:
            return -1
        for i, v in enumerate(self.table[hs]):
            if v[0] == key:
                return v[1]
        return -1
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hs = key % 200
        if len(self.table[hs]) == 0:
            return
        check = -1
        for i, v in enumerate(self.table[hs]):
            if v[0] == key:
                check = i
                break
        if check >= 0:
            self.table[hs][check] = self.table[hs][-1]
            self.table[hs].pop()


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
