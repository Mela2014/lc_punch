class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {"end":False}


    def addWord(self, word: str) -> None:
        curr = self.trie
        for ch in word:
            curr[ch] = curr.get(ch, {"end":False})
            curr = curr[ch]
        curr["end"] = True



    def search(self, word: str) -> bool:
        def helper(word, trie):
            if not word: return trie["end"]
            for i, ch in enumerate(word):
                if ch == ".":
                    for key in trie.keys():
                        if key != "end" and helper(word[i+1:], trie[key]): return True
                    return False
                elif not ch in trie:
                    return False
                trie = trie[ch]
            return trie["end"]
        return helper(word, self.trie)
