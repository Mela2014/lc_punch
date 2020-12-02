class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popidx, stk = 0, []
        for num in pushed:
            mark = True
            if num == popped[popidx]:
                mark = False
                popidx +=1
            while stk and popped[popidx] == stk[-1]:
                stk.pop()
                popidx += 1
            if mark: stk.append(num)
        return False if stk else True
