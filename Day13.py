'''
Question Description :-

Insert Interval

Given a set of non-overlapping intervals, 
insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.


Example 1:
        Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
        Output: [[1,5],[6,9]]

Example 2:
        Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
        Output: [[1,2],[3,10],[12,16]]
        Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

def insert(intervals, newInterval):

    ans = []
    i = 0

    while i<len(intervals) and newInterval[0] > intervals[i][0]:
        ans.append(intervals[i])
        i += 1

    if not ans or ans[-1][1] < newInterval[0]:
        ans.append(newInterval)
    else:
        ans[-1][1] = max(ans[-1][1], newInterval[1])

    while i < len(intervals):
        if ans[-1][1] < intervals[i][0]:
            ans.append(intervals[i])
        else:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
        i += 1

    return ans                


print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))

'''
Optimal Solution :- 

def insert(intervals, newInterval):
    found = False
    for i in range(len(intervals)):
        if intervals[i][0] > newInterval[0]:
            intervals = intervals[:i] + [newInterval] + intervals[i:]
            found = True
            break
        
    if not found:
        intervals.append(newInterval)
        
    merged = []
    for interval in intervals:
        if len(merged) != 0 and merged[-1][1] >= interval[0]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
        
    return merged
'''
