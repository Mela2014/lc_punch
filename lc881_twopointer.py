class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right, rslt = 0, len(people)-1, 0
        while left <= right:
            if people[left]+people[right] <= limit:
                left += 1
            rslt += 1
            right -= 1
        return rslt
