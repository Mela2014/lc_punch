class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not wordList or endWord not in wordList: return []
        l, word_map, visited = len(beginWord), collections.defaultdict(list), set()
        for word in wordList:
            for i in range(l):
                word_map[word[:i]+"*"+word[i+1:]].append(word)
        dque = collections.deque([[beginWord]])
        rslt = []
        while dque:
            size = len(dque)
            for _ in range(size):
                cands = dque.popleft()
                curr = cands[-1]
                visited.add(curr)
                for i in range(l):
                    for word in word_map[curr[:i]+"*"+curr[i+1:]]:
                        if word == endWord:
                            rslt.append(cands+[word])
                            break
                        if word not in visited:
                            dque.append(cands+[word])

            if rslt:
                break
        return rslt

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words, wordmap, l = set(wordList), collections.defaultdict(list), len(beginWord)
        if endWord not in words: return []
        for word in wordList:
            for i in range(l):
                wordmap[word[:i]+"*"+word[i+1:]].append(word)

        layer, visited = collections.defaultdict(list), set()
        layer[beginWord].append([beginWord])
        while layer:
            newlayer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]
                for i in range(l):
                    for nxt in wordmap[word[:i]+"*"+word[i+1:]]:
                        if nxt not in visited:
                            newlayer[nxt] += [j + [nxt] for j in layer[word]]
            visited |= set(newlayer.keys())
            layer = newlayer
        return []
