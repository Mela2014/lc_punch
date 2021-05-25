class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if not expression: return []
        op = {"+": (lambda x, y: x+y), "-": (lambda x, y: x-y), "*": (lambda x, y: x*y)}
        def helper(left, right):
            if left >= right: return expression[right]
            rslt = []
            for i in range(left, right + 1):
                if expression[i] in op:
                    leftr, rightr = helper(left, i-1), helper(i+1, right)
                    for l in leftr:
                        for r in rightr:
                            rslt.append(op[expression[i]](int(l), int(r)))
            print(left, right)
            if not rslt: rslt.append(int(expression[left:right+1]))

            return rslt
        return helper(0, len(expression)-1)
