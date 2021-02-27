class Trie:
    def __init__(self, L):
        self.root = TrieNode()
        self.maskL = L
    def insert(self, num):
        mask = 1 << self.maskL
        curr = self.root
        while mask:
            key = 1 if num & mask else 0
            if key not in curr.children:
                curr.children[key] = TrieNode()
            curr = curr.children[key]
            mask >>= 1
    def search(self, num):
        mask = 1 << self.maskL
        curr, rslt = self.root, 0
        while mask:
            key = 0 if num&mask  else 1
            if key in curr.children:
                curr = curr.children[key]
                rslt |= mask
            else:
                curr = curr.children[1-key]
            mask >>= 1
        return rslt
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums)))-2
        solTrie, rslt = Trie(L), 0
        for num in nums:
            solTrie.insert(num)
            rslt = max(rslt, solTrie.search(num))
        return rslt

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        l = len(bin(max(nums)))-2
        rslt = 0
        for i in range(l-1, -1, -1):
            mask = rslt | 1 << i
            used = set()
            for num in nums:
                curr = num & mask
                # curr ^ mask ^ curr = 0 ^ mask = mask
                if (curr ^ mask) in used:
                    rslt = mask
                    break
                used.add(curr)
        return rslt
