class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {"end":False}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {"end":False}
            curr = curr[c]
        curr["end"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.trie
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return curr["end"]

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.trie
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True
