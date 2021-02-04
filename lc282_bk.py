class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        rslt, n = [], len(num)
        def backtracking(i, curr, last, total):
            if i == n and total == target:
                rslt.append(curr)
            else:
                for j in range(i+1, n+1):
                    temp1, temp2 = int(num[i:j]), num[i:j]
                    if i == 0:
                        backtracking(j, temp2, temp1, temp1)
                    else:
                        backtracking(j, curr+"+"+temp2, temp1, total+temp1)
                        backtracking(j, curr+"*"+temp2, last*temp1,total-last + last*temp1)
                        backtracking(j, curr+"-"+temp2, -temp1,total-temp1)
                    if num[i] == "0":
                        break
        backtracking(0, "",0, 0)
        return rslt
