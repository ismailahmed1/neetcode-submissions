class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0 
        res = []

        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        
        start_time, end_time = newInterval
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            start_time = min(start_time, intervals[i][0])
            end_time = max(end_time, intervals[i][1])
            i += 1
        
        res.append([start_time, end_time])

        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res



