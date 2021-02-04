class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        rslt, n = 0, len(arr)
        hold, temp = {0:(0, 0)}, 0
        for i in range(n):
            temp = temp ^ arr[i]
            if temp in hold:
                rslt += i-hold[temp][0]+hold[temp][1]*2 + (1 if hold[temp][1] else 0)
                hold[temp] = (i+1, i-hold[temp][0])
            else:
                hold[temp] = (i+1, 0)
        return rslt





class Solution:
    def countTriplets(self, A):
        res = cur = 0
        count = {0: [1, 0]}
        for i, a in enumerate(A):
            cur ^= a
            n, total = count.get(cur, [0, 0])
            res += i * n - total
            count[cur] = [n + 1, total + i + 1]
        return res
