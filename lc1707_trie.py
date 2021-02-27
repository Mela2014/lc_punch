class Trie:
    def __init__(self, L):
        self.trie = {}
        self.L = L
    def insert(self, num):
        curr = self.trie
        mask = 1 << self.L
        while mask:
            key = 1 if num&mask else 0
            if key not in curr:
                curr[key] = {}
            curr = curr[key]
            mask >>= 1
    def search(self, num):
        curr = self.trie
        mask = 1 << self.L
        rslt = 0
        while mask:
            key = 0 if num&mask else 1
            if key in curr:
                curr = curr[key]
                rslt |= mask
            else:
                curr = curr[1-key]
            mask >>= 1
        return rslt

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        nn, nq = len(nums), len(queries)
        idx = list(range(nq))
        idx.sort(key = lambda x: queries[x][1])
        idxn = 0
        l = len(bin(max(nums[-1], max(x[0] for x in queries))))-3
        trie, rslt = Trie(l), [-1]*nq
        for idxq in idx:
            x, m = queries[idxq]
            while idxn < nn and nums[idxn] <= m:
                trie.insert(nums[idxn])
                idxn += 1
            if idxn != 0:
                rslt[idxq] = trie.search(x)
        return rslt

#https://leetcode.com/problems/maximum-xor-with-an-element-from-array/discuss/989454/Python-14-lines
def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    nums.sort()
    answer = []
    append = answer.append
    for x, m in queries:
        if nums[0] > m:
            append(-1)
            continue
        start, stop = 0, bisect_right(nums, m)
        num = 0
        bit = 2 ** m.bit_length()
        while bit:
            plus = num + bit
            if nums[start] >= plus:
                num = plus
            elif nums[stop-1] >= plus:
                cut = bisect_left(nums, plus, start, stop)
                if x & bit:
                    stop = cut
                else:
                    start = cut
                    num = plus
            bit //= 2
        append(num ^ x)
    return answer
