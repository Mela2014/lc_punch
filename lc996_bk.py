class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        maps = {x: {y for y in count if int((x+y)**0.5)**2 == x+y} for x in count}
        l = len(nums)
        def bk(curr, curr_c):
            if curr_c != 0:
                rslt = 0
                count[curr] -= 1
                for nxt in maps[curr]:
                    if count[nxt]:
                        rslt += bk(nxt, curr_c-1)
                count[curr] += 1
            else:
                rslt = 1
            return rslt
        rslt = 0
        for c in count:
            t = bk(c, l-1)
            rslt += t
        return rslt
