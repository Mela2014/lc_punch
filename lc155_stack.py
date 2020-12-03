class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stk = []


    def push(self, x: int) -> None:
        if not self._stk:
            self._stk.append((x, x))
        else:
            self._stk.append((x, min(x, self._stk[-1][1])))
        return


    def pop(self) -> None:
        if self._stk:
            self._stk.pop()


    def top(self) -> int:
        if self._stk:
            return self._stk[-1][0]


    def getMin(self) -> int:
        if self._stk:
            return self._stk[-1][1]
