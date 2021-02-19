class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        rslt, n = [], len(word)
        def backtracking(i, curr):
            if i == n:
                rslt.append("".join(curr))
            else:
                if not curr or curr[-1].isalpha():
                    backtracking(i+1, curr+['1'])
                else:
                    backtracking(i+1, curr[:-1]+[str(int(curr[-1])+1)])
                backtracking(i+1, curr+[word[i]])
        backtracking(0, [])
        return rslt


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        self.rslt, self.n, self.word = [], len(word), word
        self.backtracking(0, "", 0)
        return self.rslt

    def backtracking(self, i, curr, cnt):
        if i == self.n:
            self.rslt.append(curr+(str(cnt) if cnt else ""))
        else:
            self.backtracking(i+1, curr, cnt+1)
            self.backtracking(i+1, curr+(str(cnt) if cnt else "")+self.word[i], 0)
