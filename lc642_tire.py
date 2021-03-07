class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr["#"] = word
    def search(self, prefix):
        curr = self.root
        for ch in prefix:
            if ch not in curr:
                return []
            curr = curr[ch]
        return self.findall(curr)
    def findall(self, curr):
        rslt = []
        for key in curr:
            if key == "#":
                rslt.append(curr[key])
            else:
                rslt += self.findall(curr[key])
        return rslt
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.hotmap = collections.defaultdict(int)
        for sentence, time in zip(sentences, times):
            self.trie.insert(sentence)
            self.hotmap[sentence] += time
        self.last = ""

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.hotmap[self.last] += 1
            self.trie.insert(self.last)
            self.last = ""
            return []
        self.last += c
        rslt = self.trie.search(self.last)
        rslt.sort(key= lambda x: (-self.hotmap[x], x))
        return rslt[:3]
