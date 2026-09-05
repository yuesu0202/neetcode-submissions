class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            cur = intervals[i]
            prev = res[-1]
            if cur[0] < prev[1]:
                res.pop()
                if cur[1] <= prev[1]:
                    res.append(cur)
                else:
                    res.append(prev)
            else:
                res.append(cur)
        return len(intervals) - len(res)