class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        # get all the abbr of target stored by length
        self.target_rslt = collections.defaultdict(list)
        self.backtracking(0, [], target)
        for i in range(1, len(target)):
            for path in self.target_rslt[i]:
                for word in dictionary:
                    if self.check_abbr(path, word):
                        break
                else:
                    return "".join(path)
        return target

    def backtracking(self, i, path, target):
        '''
        generate abbreviations for target word
        '''
        if i == len(target):
            self.target_rslt[len(path)].append(path)
        else:
            if path and path[-1].isdigit():
                self.backtracking(i+1, path[:-1]+ [str(int(path[-1])+1)], target)
            else:
                self.backtracking(i+1, path+["1"], target)
            self.backtracking(i+1, path+[target[i]], target)

    def check_abbr(self, path, word):
        '''
        check if path is word's abbrevation
        '''
        cw = 0
        for ch in path:
            if cw >= len(word):
                return False
            if not ch.isdigit():
                if ch != word[cw]: return False
                cw += 1
            else:
                cw += int(ch)
        return cw == len(word)

class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        # get all the abbr of target stored by length
        self.target_rslt, n = collections.defaultdict(list), len(target)
        self.backtracking(0, 1, target, 0)
        for i in range(1, n):
            for abbr in self.target_rslt[i]:
                for word in dictionary:
                    if self.check_abbr(abbr, target, word): break
                else:
                    cnt, rslt = 0, ""
                    for j in range(n-1, -1, -1):
                        if abbr & 1:
                            cnts = "" if cnt == 0 else str(cnt)
                            rslt, cnt = target[j]+cnts+rslt, 0
                        else: cnt += 1
                        abbr >>= 1
                    if cnt: rslt = str(cnt)+rslt
                    return rslt
        return target

    def backtracking(self, i, abbr, target, l):
        '''
        generate abbreviations for target word use bitmask
        '''
        if i == len(target):
            self.target_rslt[l].append(abbr)
        else:
            if abbr&1 == 0:
                self.backtracking(i+1, abbr << 1, target, l)
            else:
                self.backtracking(i+1, abbr << 1, target, l+1)
            self.backtracking(i+1, (abbr << 1)+1, target, l+1)

    def check_abbr(self, abbr, target, word):
        '''
        check if path is word's abbrevation
        '''
        cw, n = len(word)-1, len(target)
        for i in range(n-1, -1, -1):
            if cw < 0:
                return False
            if abbr & 1 == 1 and word[cw] != target[i]:
                return False
            cw -= 1
            abbr >>= 1
        return cw == -1
