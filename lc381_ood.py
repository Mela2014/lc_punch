class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.validx = collections.defaultdict(set)
        self.collection = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.collection.append(val)
        self.validx[val].add(len(self.collection)-1)
        return len(self.validx[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.validx[val]:
            return False
        idx = self.validx[val].pop()
        self.collection[-1], self.collection[idx] = self.collection[idx], self.collection[-1]
        self.validx[self.collection[idx]].add(idx)
        self.validx[self.collection[idx]].discard(len(self.collection)-1)
        self.collection.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.collection)
