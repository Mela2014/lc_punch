class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList:
            return 0
        lword, word_map, visited = len(beginWord), defaultdict(list), {beginWord}
        queue = deque([(beginWord, 1)])
        for wrd in wordList:
            for i in range(lword):
                word_map[wrd[:i]+"*"+wrd[i+1:]].append(wrd)
        while queue:
            wrd, step = queue.popleft()
            for i in range(lword):
                for wrd_cand in word_map[wrd[:i]+"*"+wrd[i+1:]]:
                    if wrd_cand == endWord:
                        return step +1
                    if wrd_cand not in visited:
                        visited.add(wrd_cand)
                        queue.append((wrd_cand, step+1))
                    word_map[wrd[:i]+"*"+wrd[i+1:]] = []
        return 0
