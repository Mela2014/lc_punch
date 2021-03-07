class TrieNode:
    def __init__(self):
        self.ch = {}
        self.cands = []
        self.idx = -1
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word, idx):
        curr = self.root
        for i in range(len(word)-1, -1, -1):
            if word[:i+1] == word[:i+1][::-1]:
                curr.cands.append(idx)
            if word[i] not in curr.ch:
                curr.ch[word[i]] = TrieNode()
            curr = curr.ch[word[i]]
        curr.idx = idx
        curr.cands.append(idx)
    def search(self, word, idx):
        curr = self.root
        rslt = []
        for i in range(len(word)):
            if word[i:] == word[i:][::-1] and curr.idx != idx and curr.idx > -1:
                rslt.append([idx, curr.idx])
            ch = word[i]
            if ch not in curr.ch:
                return rslt
            curr = curr.ch[ch]
        for cand in curr.cands:
            if cand != idx:
                rslt.append([idx, cand])
        return rslt
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        paltrie = Trie()
        rslt = []
        for i, word in enumerate(words):
            paltrie.insert(word, i)
        for i, word in enumerate(words):
            rslt += paltrie.search(word, i)
        return rslt
