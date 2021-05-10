class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        nxt_h, nxt_l = [0]*n, [0]*n
        stack = []
        for i in sorted(range(n), key = lambda x: (arr[x], x)):
            while stack and stack[-1] < i:
                nxt_h[stack.pop()] = i
            stack.append(i)

        stack = []
        for i in sorted(range(n), key = lambda x: (-arr[x], x)):
            while stack and stack[-1] < i:
                nxt_l[stack.pop()] = i
            stack.append(i)

        nh, nl = [0]*n, [0]*n
        nh[-1], nl[-1] = 1, 1
        for j in range(n-2, -1, -1):
            nh[j] = nl[nxt_h[j]]
            nl[j] = nh[nxt_l[j]]
        return sum(nh)
