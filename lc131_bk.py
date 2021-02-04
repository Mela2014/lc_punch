class Solution:
    def partition(self, s: str) -> List[List[str]]:
        rslt, n, checked = [], len(s), set()
        def backtracking(left, curr):
            if left == n:
                rslt.append(curr)
            else:
                for j in range(left, n):
                    temp = s[left:j+1]
                    if temp == temp[::-1]:
                        backtracking(j+1, curr+[temp])
        backtracking(0, [])
        return rslt
