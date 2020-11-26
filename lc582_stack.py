class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        mmap = collections.defaultdict(list)
        for child, parent in zip(pid, ppid):
            mmap[parent].append(child)
        rslt, stk = [], [kill]
        while stk:
            temp = stk.pop()
            rslt.append(temp)
            for child in mmap[temp]:
                stk.append(child)
        return rslt
