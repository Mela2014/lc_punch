class Node:
    def __init__(self, val = 0,key = 0,  left = None, right = None):
        self.val = val
        self.key = key
        self.left = left
        self.right = right
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.end = Node(left = self.head)
        self.head.right = self.end
        self.maps = {}

    def get(self, key: int) -> int:
        if not self.maps or key not in self.maps:
            return -1
        curr = self.maps[key]
        curr.left.right = curr.right
        curr.right.left = curr.left
        curr.left = self.end.left
        curr.right = self.end
        self.end.left = curr
        curr.left.right = curr
        return curr.val

    def put(self, key: int, value: int) -> None:
        if key in self.maps:
            self.maps[key].val = value
            _ = self.get(key)
        else:
            curr = Node(val = value, key = key , left = self.end.left, right = self.end)
            self.end.left.right = curr
            self.end.left = curr
            self.maps[key] = curr
            if self.capacity == 0:
                temp = self.head.right
                self.head.right = self.head.right.right
                self.head.right.left = self.head
                self.maps.pop(temp.key)
            else:
                self.capacity -= 1
