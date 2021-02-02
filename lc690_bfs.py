class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hold = {x.id: i for i, x in enumerate(employees)}
        dque = collections.deque([id])
        visited, rslt = {id}, 0
        while dque:
            curr = dque.popleft()
            employee = employees[hold[curr]]
            rslt += employee.importance
            for n in employee.subordinates:
                if n not in visited:
                    visited.add(n)
                    dque.append(n)
        return rslt 
