class Node:
    def __init__(self, val = 0, key = 0, freq = 1):
        self.val = val
        self.key = key
        self.left = self.right = None
        self.freq = 1

class Dll:
    def __init__(self):
        self.snode = Node()
        self.snode.left  =self.snode.right = self.snode
        self.size = 0
    def append(self, node):
        node.left = self.snode.left
        node.right = self.snode
        self.snode.left = node
        node.left.right = node
        self.size += 1
    def remove(self, node):
        node.left.right = node.right
        node.right.left = node.left
        node.left, node.right = None, None
        self.size -= 1
    def pop(self):
        temp = self.snode.right
        self.remove(temp)
        return temp

class LFUCache:

    def __init__(self, capacity: int):
        self.keynode = {}
        self.freq = collections.defaultdict(Dll)
        self.capacity = capacity
        self.min_freq = 1
    def get(self, key: int) -> int:
        if key not in self.keynode: return -1
        curr = self.keynode[key]
        dll = self.freq[curr.freq]
        dll.remove(curr)
        curr.freq += 1
        self.freq[curr.freq].append(curr)
        if self.freq[self.min_freq].size == 0:
            self.min_freq += 1
        return curr.val
    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.keynode:
            self.keynode[key].val = value
            self.get(key)
        else:
            if self.capacity == len(self.keynode):
                temp = self.freq[self.min_freq].pop()
                self.keynode.pop(temp.key)
            curr = Node(val = value, key = key)
            self.keynode[key] = curr
            self.freq[1].append(curr)
            self.min_freq = 1
