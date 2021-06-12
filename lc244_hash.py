class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.maps = collections.defaultdict(list)
        self.cache = {}
        for i, word in enumerate(wordsDict):
            self.maps[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        if (word1, word2) in self.cache: return self.cache[(word1, word2)]
        if (word2, word1) in self.cache: return self.cache[(word2, word1)]
        cand1, cand2 = self.maps[word1], self.maps[word2]
        # if len(cand1) > len(cand2): cand1, cand2 = cand2, cand1
        # rslt = float("inf")
        # for x in cand1:
        #     y = bisect.bisect(cand2, x)
        #     if y < len(cand2):
        #         rslt = min(rslt, cand2[y]-x)
        #     if y > 0: rslt = min(rslt, x-cand2[y-1])
        # return rslt
        l1, l2 = 0, 0
        rslt = float("inf")
        while l1 < len(cand1) and l2 < len(cand2):
            rslt = min(rslt, abs(cand1[l1]-cand2[l2]))
            if cand1[l1] < cand2[l2]:
                l1 += 1
            else:
                l2 += 1
        self.cache[(word1, word2)] = rslt
        return rslt
