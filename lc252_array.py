class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i, it in enumerate(intervals):
            if i > 0 and it[0] < intervals[i-1][1]:
                return False
        return True
