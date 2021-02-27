class TrieNode:
    def __init__(self):
        self.next = {}
        self.idx = set()
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word, idx):
        curr = self.root
        for ch in word:
            if ch not in curr.next:
                curr.next[ch] = TrieNode()
            curr.next[ch].idx.add(idx)
            curr = curr.next[ch]
    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.next:
                 return set()
            curr = curr.next[ch]
        return curr.idx
class WordFilter:

    def __init__(self, words: List[str]):
        self.TriePre = Trie()
        self.TriePost = Trie()
        l, seen = len(words), set()
        for j in range(l-1, -1, -1):
            word = words[j]
            if word not in seen:
                seen.add(word)
                self.TriePre.insert(word, j)
                self.TriePost.insert(word[::-1], j)

    def f(self, prefix: str, suffix: str) -> int:
        preset = self.TriePre.search(prefix)
        postset = self.TriePost.search(suffix[::-1])
        rslt = preset & postset
        return max(rslt) if rslt else -1


class TrieNode:
    def __init__(self, idx = -1):
        self.next = {}
        self.idx = -1
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word, idx):
        curr = self.root
        for ch in word:
            if ch not in curr.next:
                curr.next[ch] = TrieNode()
            curr.next[ch].idx = idx
            curr = curr.next[ch]
    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.next:
                return -1
            curr = curr.next[ch]
        return curr.idx
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for j, word in enumerate(words):
            for i in range(len(word)):
                self.trie.insert(word[i:]+"#"+word, j)
    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.search(suffix+"#"+prefix)
